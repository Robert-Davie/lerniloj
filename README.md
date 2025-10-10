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
uv run src/flashcards_v2.py
```
the flashcard scenarios (e.g. french, written, 100 terms) etc are controlled through the ```flashcard_settings.toml``` file present in the root directory.

