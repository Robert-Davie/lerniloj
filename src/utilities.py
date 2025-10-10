import re


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


german_accent_shortcuts = (
    ("ä", "a:"),
    ("ö", "o:"), 
    ("ü", "u:"), 
    ("ß", "ss!")
)


accents = {
    "french": french_accent_shortcuts,
    "esperanto": esperanto_accent_shortcuts,
    "german": german_accent_shortcuts,
}


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


def toggle_accents(str_in: str, foreign_language_in: str, is_adding_accents: bool) -> str:
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
            str_in = str_in.replace(accent_definition[0], accent_definition[1]).replace("!", "")
    return str_in