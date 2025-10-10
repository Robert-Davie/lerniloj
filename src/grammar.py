import random


ITERATIONS = 100


def number_of_similarities(l1, l2):
    maximum = min(len(l1), len(l2))
    res = 0
    for position in range(maximum):
        if l1[position] == l2[position]:
            res += 1
    return res



with open("the_little_prince.txt","r") as f:
    lines = [line.strip() for line in f.readlines()]
    text = " ".join(lines).replace("’", "'")

sentences = [sentence.lower() for sentence in text.split(". ") if sentence != ""]
sentences = [s for s in sentences if " l'" in s or " le " in s or " la " in s or " les " in s]
sentences = list(set(sentences))

correct = 0
total = 0
for iteration in range(ITERATIONS):
    answer_count = 0
    while answer_count == 0:
        print(f"{correct} / {total}    Q{iteration + 1}")
        sentence = random.choice(sentences)
        answers = []
        question_sentence = []
        words = sentence.split()
        for position, word in enumerate(words):
            if word in ["le", "la", "les"]:
                if position >= 1 and words[position - 1] not in ["je", "tu", "il", "elle", "on", "nous", "vous", "ils", "elles"]:
                    answers.append(word)
                    question_sentence.append("___")
            elif len(word) > 2 and word[:2] == "l'":
                answers.append("l'")
                question_sentence.append("___")
                question_sentence.append(word[2:])
            else:
                question_sentence.append(word)
        answer_count = len(answers)
    final_question = " ".join(question_sentence) + f"\nplease give {answer_count} answer{'s' if answer_count > 1 else ''}\n"
    user_answer = ""
    while user_answer == "":
        user_answer = input(final_question)
        if len(user_answer.split()) != len(answers):
            user_answer = ""
            print("wrong number of answers, please answer again\n")
    correct += number_of_similarities(user_answer.split(), answers)
    total += answer_count
    if user_answer.lower() == " ".join(answers):
        print("correct\n")
    else:
        print("incorrect")
        print(f"""answers = {" ".join(answers)}\n""")
print(f"you got {correct} out of {total}")
print(f"{round((correct / total) * 100, 2)}%")