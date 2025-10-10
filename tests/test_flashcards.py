from lerniloj.flashcards import get_question, parse_line, get_number_of_correct_responses


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
