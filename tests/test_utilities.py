from lerniloj.utilities import decompose_esperanto_word


def test_decompose_esperanto_lernilo():
    term = "lernilo"
    breakdown, _ = decompose_esperanto_word(term)
    assert breakdown == ["lern", "il", "o"]


def test_decompose_kunvivi():
    term = "kunvivi"
    breakdown, _ = decompose_esperanto_word(term)
    assert breakdown == ["kun", "viv", "i"]


def test_decompose_transformado():
    term = "transformado"
    breakdown, _ = decompose_esperanto_word(term)
    assert breakdown == ["trans", "form", "ad", "o"]