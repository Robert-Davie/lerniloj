import json
import random
from ignorable.flashcards_original import substitute_accents


ITERATIONS = 10


with open("verb_conjugations.json", "r") as f:
    data = json.load(f)

with open("verb_conjugations_regularity.json", "r") as f:
    regular_verbs = json.load(f)


correct = 0
for iteration in range(ITERATIONS):
    is_regular = random.choice([True, False])
    if is_regular:
        verb_type = random.choice([".er", ".ir"])
        word = random.choice(regular_verbs[verb_type])
    else:
        word = random.choice([word for word in data])
    if is_regular:
        word_json = data[verb_type]
    else:
        word_json = data[word]
    stem = word[:-2]
    tense = random.choice(
        [
            "present",
            "future",
            "imperfect",
            "subjunctive",
            "conditional",
            "passé simple",
            "imperative",
        ]
    )
    if tense == "imperative":
        pronoun = random.choice(["tu", "nous", "vous"])
    else:
        pronoun = random.choice(
            ["je", "tu", "il", "elle", "on", "nous", "vous", "ils", "elles"]
        )

    extension = "non_nv_stem"

    user_answer = ""
    while user_answer == "":
        user_answer = input(f"{word} \npronoun={pronoun} \ntense='{tense}'\n")
    user_answer = substitute_accents(user_answer)
    user_answer = user_answer.replace("$", word[:-2])
    if pronoun in ["je", "tu"]:
        lookup_pronoun = pronoun
    elif pronoun in ["nous", "vous"]:
        lookup_pronoun = pronoun
        extension = "nv_stem"
    elif pronoun in ["il", "elle", "on"]:
        lookup_pronoun = "il/elle/on"
    elif pronoun in ["ils", "elles"]:
        lookup_pronoun = "ils/elles"
    else:
        print("could not find lookup pronoun")
    answer = (
        word_json[tense]["stem"]
        + word_json[tense][extension]
        + word_json[tense][lookup_pronoun]
    )
    answer = answer.replace(".", stem)
    print(f"{user_answer} == {answer}")
    if user_answer == answer:
        print("correct\n")
        correct += 1
    else:
        print(f"incorrect answer = {answer}\n")
print(f"you got {correct} out of {ITERATIONS}, {round(correct * 100 / ITERATIONS, 2)}%")
