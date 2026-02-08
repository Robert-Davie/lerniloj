# from lerniloj.utilities import decompose_esperanto_word, get_esperanto_word_type, EoType, EoSpecialType, get_multiple_esperanto_word_types
from lerniloj.utilities import remove_accents


def test_remove_accents():
    assert remove_accents("béd", "french") == "bed"


# def test_decompose_esperanto_lernilo():
#     term = "lernilo"
#     breakdown, _, _ = decompose_esperanto_word(term)
#     assert breakdown == ["lern", "il", "o"]


# def test_decompose_kunvivi():
#     term = "kunvivi"
#     breakdown, _, _ = decompose_esperanto_word(term)
#     assert breakdown == ["kun", "viv", "i"]


# def test_decompose_transformado():
#     term = "transformado"
#     breakdown, _, _ = decompose_esperanto_word(term)
#     assert breakdown == ["trans", "form", "ad", "o"]


# def test_decompose_ŝokanta():
#     term = "ŝokanta"
#     breakdown, _, _ = decompose_esperanto_word(term)
#     assert breakdown == ["ŝok", "ant", "a"]


# def test_get_esperanto_word_type_lerni():
#     assert get_esperanto_word_type("lerni") == EoType.VERB_INFINITIVE


# def test_get_esperanto_word_type_lernas():
#     assert get_esperanto_word_type("lernas") == EoType.V_PRES


# def test_get_word_types_of_text():
#     a = get_multiple_esperanto_word_types("Antikvegiptaj fabloj ne estis verkitaj uzante hieroglifojn")
#     b = [
#         EoType.ADJ_PL,
#         EoType.N_PL,
#         EoSpecialType.NE,
#         EoType.V_PAST,
#         EoType.ADJ_PL,
#         EoType.ADV,
#         EoType.N_PLAC
#     ]
#     assert a == b


# def test_noun_plural_accusative():
#     a = get_multiple_esperanto_word_types("hieroglifojn")
#     b = [
#         EoType.N_PLAC,
#     ]
#     assert a == b

# def test_get_word_types_of_text_with_full_stop():
#     a = get_multiple_esperanto_word_types("hieroglifojn.")
#     b = [
#         EoType.N_PLAC,
#         EoSpecialType.FULL_STOP
#     ]
#     assert a == b
