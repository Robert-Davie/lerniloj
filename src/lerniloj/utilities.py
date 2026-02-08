import re
from enum import Enum
from lerniloj import esperanto_roots


french_accent_shortcuts = (
    ("é", "e'"),
    ("ç", "c,"),
    ("à", "a`"),
    ("â", "a^"),
    ("ë", "e:"),
    ("î", "i^"),
    ("ï", "i:"),
    ("ô", "o^"),
    ("û", "u^"),
    ("è", "e`"),
    ("ê", "e^"),
    ("œ", "oe!"),
    ("ù", "u`"),
    ("ÿ", "y:"),
    ("é", "£"),
)


esperanto_accent_shortcuts = (
    ("ĉ", "cx"),
    ("ĝ", "gx"),
    ("ĥ", "hx"),
    ("ĵ", "jx"),
    ("ŝ", "sx"),
    ("ŭ", "ux"),
)


german_accent_shortcuts = (("ä", "a:"), ("ö", "o:"), ("ü", "u:"), ("ß", "ss!"))


accents = {
    "french": french_accent_shortcuts,
    "esperanto": esperanto_accent_shortcuts,
    "german": german_accent_shortcuts,
}


def remove_accents(str_in: str, language: str) -> str:
    for a in accents[language]:
        str_in = str_in.replace(a[0], a[1][:-1])
    return str_in


def remove_punctuation(str_in: str) -> str:
    """remove excess punctuation from a string, except hyphens which are replaced with spaces

    Args:
        str_in (str): the string with excess punctuation

    Returns:
        str: the string without excess punctuation
    """
    str_in = str_in.replace("-", " ")
    return re.sub(r"[^\w\s']", "", str_in)


def get_accent_shortcuts_one_line(foreign_language_in: str) -> str:
    """provides a one line list of all accent shortcuts on keyboard for a given language

    Args:
        foreign_language_in (str): foreign_language the shortcuts should be from

    Returns:
        str: the one line string of all shortcuts in given language
    """
    return "   ".join([f"{i[0]}={i[1]}" for i in accents[foreign_language_in]])


def remove_gender_abbreviations(str_in: str) -> str:
    """remove the gender abbreviations ' f', ' m', ' fpl' and ' mpl' at the end of the string

    Args:
        str_in (str): string to be cleaned

    Returns:
        str: string with abbreviations removed
    """
    return re.sub(r"\sf$|\sm$|\sfpl$|\smpl$", "", str_in)


def toggle_accents(
    str_in: str, foreign_language_in: str, is_adding_accents: bool
) -> str:
    """convert to or from accent form, based on accent shortcuts

    Args:
        str_in (str): string to be converted
        foreign_language_in (str): the foreign language to be used
        is_adding_accents (bool): if True converts shortcuts to accents, otherwise removes all accents

    Returns:
        str: cleaned string
    """
    for accent_definition in accents[foreign_language_in]:
        if is_adding_accents:
            str_in = str_in.replace(accent_definition[1], accent_definition[0])
        else:
            # removing accents
            str_in = str_in.replace(accent_definition[0], accent_definition[1]).replace(
                "!", ""
            )
    return str_in


with open("word_lists/esperanto_roots.txt", "r") as f:
    esperanto_root_templates = [i.strip().split(",") for i in f.readlines()]


def decompose_esperanto_word(str_in: str) -> tuple[list[str], list[str], bool]:
    breakdown = []
    meanings = []

    final_part_found = False
    if str_in[-1] == "n":
        breakdown.append("n")
        meanings.append("")
        str_in = str_in[:-1]
    if str_in[-1] == "j":
        breakdown.append("j")
        meanings.append("")
        str_in = str_in[:-1]
    for final_part in esperanto_roots.final_parts:
        if str_in[-len(final_part[0]):] == final_part[0]:
            breakdown.append(final_part[0])
            meanings.append("")
            final_part_found = True
            str_in = str_in[:-(len(final_part[0]))]
            break
    if not final_part_found:
        return breakdown, meanings, False

    for i in range(3):
        if len(str_in) == 0:
            return breakdown[::-1], meanings[::-1], True
        finished = False
        while finished == False:
            suffix_count = 0
            for suffix in esperanto_root_templates:
                if str_in[-len(suffix[0]):] == suffix[0]:
                    breakdown.append(suffix[0])
                    meanings.append(suffix[1])
                    str_in = str_in[:-(len(suffix[0]))]
                    break
                suffix_count += 1
            if suffix_count == len(esperanto_root_templates):
                finished = True
                break
        
        if len(str_in) > 2 and str_in[-1] == "t" and str_in[-2] in ['a', 'i', 'o']:
            breakdown.append(str_in[-2:])
            meanings.append("")
            str_in = str_in[:-2]
        if len(str_in) > 3 and str_in[-2:] == "nt" and str_in[-3] in ['a', 'i', 'o']:
            breakdown.append(str_in[-3:])
            meanings.append("")
            str_in = str_in[:-3]

        finished = False
        while finished == False:
            suffix_count = 0
            for suffix in esperanto_roots.suffixes:
                if str_in[-len(suffix[0]):] == suffix[0]:
                    breakdown.append(suffix[0])
                    meanings.append(suffix[1])
                    str_in = str_in[:-(len(suffix[0]))]
                    finished = True
                    break
                suffix_count += 1
            if suffix_count == len(esperanto_roots.suffixes):
                finished = True
                break

    term_prefix = None
    for prefix in esperanto_roots.prefixes:
        if str_in[:len(prefix[0])] == prefix[0]:
            str_in = str_in[(len(prefix[0])):]
            term_prefix = prefix
            break
    solved = True
    if str_in != "":
        breakdown.append(str_in)
        meanings.append(str_in)
        solved = False
    if term_prefix:
        breakdown.append(term_prefix[0])
        meanings.append(term_prefix[1])
    return breakdown[::-1], meanings[::-1], solved