from lerniloj.flashcards import get_question, parse_line, get_number_of_correct_responses, is_user_response_correct, get_user_response_to_question, compute_user_response_shortcuts
from unittest.mock import patch


def test_get_question_in_english():
    question = get_question("argent;silver", question_in_english=True)
    assert question == "silver"


def test_get_question_in_english_multiple_options():
    question = get_question("foo;bar1, bar2", question_in_english=True)
    assert question == "bar1, bar2"


def test_get_question_in_french():
    question = get_question("argent;silver", question_in_english=False)
    assert question == "argent"


def test_get_question_in_french_with_hint():
    question = get_question("argent;silver*argentina", question_in_english=False)
    assert question == "argent"


def test_parse_line():
    result = parse_line("xyz;abc, def *ghi jkl")
    assert result == ("xyz", ["abc", "def"], "ghi jkl")


def test_get_number_of_correct_responses():
    input_in = [{"is_correct": True}, {"is_correct": False}, {"is_correct": True}]
    result = get_number_of_correct_responses(input_in)
    assert result == 2


def test_is_user_response_correct_multiple_foreign_terms():
    line = "a, b;c, d *efgh ijk lm"
    assert is_user_response_correct(line, "a", True, "german") == True
    assert is_user_response_correct(line, "b", True, "german") == True
    assert is_user_response_correct(line, "c", True, "german") == False


def test_compute_user_response_shortcuts_dot():
    assert compute_user_response_shortcuts(".", "abcdéf") == "abcdef"


def test_compute_user_response_shortcuts_dot_3():
    assert compute_user_response_shortcuts(".3", "abcdéf") == "abc"


def test_compute_user_response_shortcuts_dot_3_plus_letters():
    assert compute_user_response_shortcuts(".3fgh", "abcdéf") == "abcfgh"