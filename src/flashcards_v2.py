import re
import random
import datetime
import os
import json
import traceback
import tomllib
import utilities
from dataclasses import make_dataclass


def get_question(line_in: str, question_in_english: bool) -> str:
    foreign_term, english_terms, _ = parse_line(line_in)
    english_terms = ", ".join(english_terms)
    if question_in_english:
        question = english_terms
    else:
        question = foreign_term
    return question


def get_user_response_to_question(line_in: str, question_in_english: bool) -> str:
    response = ""
    while response == "":
        question = get_question(line_in, question_in_english)
        response = input(question + "\n").lower().strip()
    return response


def is_user_response_correct(
    line_in: str, 
    user_response_in: str, 
    is_question_in_english_in: bool, 
    foreign_language_in: str
) -> tuple[bool]:
    foreign_term, english_terms, hint = parse_line(line_in)
    foreign_term = utilities.remove_gender_abbreviations(foreign_term)
    if hint:
        print(f"hint: hint")
    if is_question_in_english_in:
        foreign_term = utilities.remove_punctuation(foreign_term)
        user_response_in = utilities.toggle_accents(user_response_in, foreign_language_in, True)
        print(f"formatted: {user_response_in}")
        return user_response_in == foreign_term
    else:
        user_response_in = utilities.toggle_accents(user_response, foreign_language_in, False)
        return user_response_in in english_terms or f"to {user_response_in}" in english_terms


def parse_line(line_in: str) -> tuple[str|list[str]]:
    foreign_term = line_in.split(";")[0]
    english_terms = line_in.split(";")[1].split("*")[0].split(",")
    english_terms = [term.strip() for term in english_terms]
    if "*" in line_in:
        hint = line_in.split(";")[1].split("*")[1]
    else:
        hint = ""
    return foreign_term, english_terms, hint


def get_number_of_correct_responses(user_responses_in: list[dict[bool|str]]) -> int:
    return sum(1 for response in user_responses_in if response["is_correct"])


def get_correct_answer(line_in: str, is_question_in_english_in: bool) -> str:
    return parse_line(line_in)[0] if is_question_in_english_in else ", ".join(parse_line(line_in)[1])


if __name__ == "__main__":
    # load settings
    with open("flashcard_settings.toml", "rb") as f:
        settings = tomllib.load(f)
    for attribute, value in settings.items():
        print(attribute, value)

    is_question_in_english = settings["give_question_in_english"]
    
    # load terms
    reference_file = settings["reference_file"]
    with open(f"word_lists/{reference_file}", "r") as f:
        lines = [line.strip() for line in f.readlines() if line != ""]
        assert re.fullmatch("^LANGUAGE=[A-Z]*$", lines[0])
        foreign_language = lines[0].split("=")[1].lower()
        lines = lines[1:]
    
    if settings["audio_mode"]:
        assert is_question_in_english == False
        assert foreign_language == "french"

    # helpful reference of accent shortcuts
    if is_question_in_english:
        print(utilities.get_accent_shortcuts_one_line(foreign_language))

    user_responses = []
    for iteration in range(settings["iterations"]):
        try:
            print(f"{get_number_of_correct_responses(user_responses)} / {iteration}")
            line = random.choice(lines)
            user_response = get_user_response_to_question(line, is_question_in_english)
            is_correct = is_user_response_correct(line, user_response, is_question_in_english, foreign_language)
            if is_correct:
                print("correct\n")
            else:
                correct_answer = get_correct_answer(line, is_question_in_english)
                print(f"incorrect - answer is '{correct_answer}'\n")
            user_responses.append({
                "is_correct": is_correct,
                "user_response": user_response,
                "line": line,
            })
        except Exception as e:
            # to prevent error from causing loss of all progress
            print(f"an error occurred: {e}, {traceback.format_exc()}")
    print("FINISHED")
    print(f"you got {get_number_of_correct_responses(user_responses)} out of {settings["iterations"]} correct\n")
    if get_number_of_correct_responses(user_responses) == settings["iterations"]:
        # no mistakes to revisit
        quit()
    # repeating previous wrong answers
    previous_mistakes = [response for response in user_responses if response["is_correct"] == False]
    previous_mistakes = previous_mistakes[::-1]
    print("repeating previous wrong answers")
    print("type 'skip' to skip a question")
    while previous_mistakes != []:
        print(f"{len(previous_mistakes)} mistakes remaining")
        previous_mistake = previous_mistakes.pop()
        line = previous_mistake["line"]
        user_response = get_user_response_to_question(line, is_question_in_english)
        if user_response == "skip":
            print("skipping question")
            continue
        is_correct = is_user_response_correct(line, user_response, is_question_in_english, foreign_language)
        if is_correct:
            print("correct\n")
        if not is_correct:
            correct_answer = get_correct_answer(line, is_question_in_english)
            print(f"incorrect - answer is {correct_answer}\n")
            previous_mistakes.insert(0, previous_mistake)
        
    
    
