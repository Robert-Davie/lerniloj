import re


def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)


with open("salome.txt", "r") as f:
    lines = [i.strip() for i in f.readlines()]

words = []
for line in lines:
    words.extend(line.replace("-", " ").replace("’", " ").split())
words = [re.sub("\W", "", word) for word in words]
words = sorted(list(set(words)))


with open("phrases2.txt", "r") as f:
    phrases = f.readlines()
    phrase_text = " ".join(phrases)


with open("5000wordsv2.txt") as f:
    phrases = f.readlines()
    phrase_text = phrase_text + " ".join(phrases)


words = [word for word in words if word not in phrase_text]
words = [word for word in words if word.lower() == word]

temp = []
for word in words:
    if word[-1] == "s":
        if word[:-1] in phrase_text or word[:-1] in words:
            continue
    if word[-1] == "é":
        continue
    if word[-2:] in ["ée", "ai", "ez", "as", "ra"]:
        continue
    if word[-3:] in ["ent", "ons", "ont", "ais", "ait", "ées", "ant", "ira", "era"]:
        continue
    if word[-4:] in ["iant", "ions"]:
        continue
    temp.append(word)

words = temp
for word in words:
    print(word)
with open("salome4.txt", "w") as f:
    f.writelines([word + "\n" for word in words])

print(len(words))

# for line_number, line in enumerate(lines):
#     if line_number == 0:
#         continue
#     previous_line = lines[line_number-1]
#     if any([
#         has_numbers(line + previous_line),
#         "|" in line + previous_line,
#         len(previous_line) > 3 and previous_line[:3] in ["la ", "le "],
#         len(previous_line) > 4 and previous_line[:4] in ["les "],
#         len(line) > 3 and line[:3] in ["to "],
#         len(previous_line) > 3 and previous_line[-2:] in [" f", " m"],
#         len(previous_line) > 4 and previous_line[-4:] in [" mpl", " fpl"],
#         "/" in line + previous_line,
#         "é" in previous_line,
#         "ë" in previous_line,
#         line == "vocabulary" or previous_line == "vocabulary",
#     ]):
#         continue
#     print(f"{line};{previous_line}")
# line = re.sub("\d", "", line)
# words = line.split()
# print(f"{words[0]}    ({words[1]});{" ".join(words[2:])}")
# match = re.search("\d+\\.\s(\D+)to\s(\D+)", line.lower())
# simplified = match.group(0).split(".")[1].strip()
# print(f"{simplified.split()[0]};{" ".join([i.strip() for i in simplified.split()[1:]])}".replace(" - ",", "))
