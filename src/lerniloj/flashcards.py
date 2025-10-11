import re
import random
import datetime
import csv
import json
from pathlib import Path
import traceback
import tomllib
from typing import Any

from lerniloj import utilities
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
    foreign_term = utilities.remove_gender_abbreviations(foreign_term).lower()
    english_terms = [term.lower() for term in english_terms]
    if hint:
        print(f"hint: hint")
    if is_question_in_english_in:
        foreign_terms = [i.strip() for i in foreign_term.split(",")]
        foreign_term = utilities.remove_punctuation(foreign_term)
        user_response_in = utilities.toggle_accents(user_response_in, foreign_language_in, True)
        print(f"formatted: {user_response_in}")

        return user_response_in == foreign_term or user_response_in in foreign_terms
    else:
        user_response_in = utilities.toggle_accents(user_response_in, foreign_language_in, False)
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


def save_results(
    settings_in: dict[str, Any],
    correct_count: int,
    foreign_language: str,
):
    save_file_location = settings_in["save_results_file"]
    file_already_exists = Path(save_file_location).is_file()
    with open(save_file_location, "a") as f:
        reference_file = settings_in["reference_file"]
        iterations = settings_in["iterations"]
        audio_mode = settings_in["audio_mode"]
        current_time = datetime.datetime.now()
        question_language = "english" if settings_in["give_question_in_english"] else foreign_language
        result = [reference_file, correct_count, iterations, audio_mode, current_time, question_language, foreign_language]
        writer = csv.writer(f)
        if not file_already_exists:
            # write header
            writer.writerow(["reference_file", "correct_count", "iterations", "audio_mode", "current_time", "question_language", "foreign_language"])
        writer.writerow(result)
    
    print("saved result successfully")


def add_value_to_json(
    json_data_in: dict,
    is_correct_in: bool,
    unix_time_in: int,
    user_answer_in: str,
    quiz_type_in: str,
    foreign_term_in: str,
) -> None:
    value = {"correct": is_correct_in, "date": unix_time_in}
    if not is_correct_in:
        value["user_answer"] = user_answer_in
    
    if not quiz_type_in in json_data_in.keys():
        json_data_in[quiz_type_in] = {}
    if foreign_term_in in json_data_in[quiz_type_in].keys():
        json_data_in[quiz_type_in][foreign_term_in].append(value)
    else:
        json_data_in[quiz_type_in][foreign_term_in] = [value]


def save_to_answer_history(
    settings_in: dict[str, Any],
    answers_in: list[dict[str]]
):
    answer_history_file = settings_in["answer_history_file"]
    if Path(answer_history_file).exists():
        with open(answer_history_file, "r") as f:
            data = json.load(f)
    else:
        data = {}
    quiz_type = "to" if settings_in["give_question_in_english"] else "from"
    quiz_type += f"_{settings_in["foreign_language"]}_"
    quiz_type += "oral" if settings_in["audio_mode"] else "written"
    current_time_unix = int(datetime.datetime.now().timestamp())
    
    for answer in answers_in:
        foreign_term, _, _ = parse_line(answer["line"])
        add_value_to_json(data, answer["is_correct"], current_time_unix, answer["user_response"], quiz_type, foreign_term)
    
    print("dumping to json")

    with open(answer_history_file, "w") as f:
        json.dump(data, f, indent=4)
    print("saved answers")


def flashcard():
    # load settings
    if not Path("flashcard_settings.json").exists():
        with open("flashcard_settings.json", "w") as f:
            settings = {
                "iterations": 100,
                "reference_file": "german2000.txt",
                "record_mistakes": True,
                "audio_mode": False,
                "save_results": True,
                "give_question_in_english": False,
                "save_results_file": "reports/results2.csv",
                "answer_history_file": "history/mistakes2.json"
            }
            json.dump(settings, f, indent=4)
    else:
        with open("flashcard_settings.json", "r") as f:
            settings = json.load(f)
    
    for attribute, value in settings.items():
        print(attribute, value)

    is_question_in_english = settings["give_question_in_english"]
    
    # load terms
    reference_file = settings["reference_file"]
    with open(f"word_lists/{reference_file}", "r") as f:
        lines = [line.strip() for line in f.readlines() if line != ""]
        assert re.fullmatch("^LANGUAGE=[A-Z]*$", lines[0])
        foreign_language = lines[0].split("=")[1].lower()
        settings["foreign_language"] = foreign_language
        lines = lines[1:]
    
    if settings["audio_mode"]:
        assert is_question_in_english == False
        assert foreign_language == "french"

    # print helpful reference of accent shortcuts
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
    correct_count = get_number_of_correct_responses(user_responses)
    print(f"you got {correct_count} out of {settings["iterations"]} correct\n")
    if settings["save_results"]:
        save_results(settings, correct_count, foreign_language)
    if settings["record_mistakes"]:
        try:
            save_to_answer_history(settings, user_responses)
        except Exception as e:
            print(e.with_traceback())
            print("an error occurred whilst trying to save user responses to answer history")
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
            print(f"incorrect - answer is '{correct_answer}'\n")
            previous_mistakes.insert(0, previous_mistake)
        
    
    
