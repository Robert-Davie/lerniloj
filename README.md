# Lerniloj 
(eo: learn tools)

A set of language learning applications, designed to make it easy to learn new languages in a style similar to anki. The application comes with some premade testing sets for French and Esperanto.

## Installation
1. make sure you have python installed
2. install uv (modern python dependency manager)
3. clone the project ```git clone <link to the project>```
4. setup venv
```uv venv```

## Flashcard Application
to use the flashcard application please run
```
uv run src/lerniloj/main.py
```
the flashcard scenarios (e.g. french, written, 100 terms) etc are controlled through the ```flashcard_settings.json``` file present in the root directory.
the settings file is created with defaults by running the program if it does not already exist.

## Development
to run tests use pytest
```uv run pytest```

## Languages
the following languages are supported (aside from English):
* Esperanto
* French
* German
to add more languages is simply a matter of creating accent shortcuts and writing out lists of words

## Word Lists
lists of words to be memorized are found in the word_lists folder
the top of the file specifies the language
all terms are written out in the form ```<foreign_term>, <second_foreign_term (optional) ...;<english_term>, <second_english_term (optional) ...*<helpful_hint>```