import random

# Getting Eugene Onegin text with whitespaces
with open("/home/alexey/IT/Experiment_text_generator/EugeneOnegin.txt", "r") as f:
    text = f.read().replace("\n", "")

letters = dict()
for l in text:
    if l not in letters: letters[l] = 1
    else: letters[l] += 1

letters = dict(sorted(letters.items(), key=lambda x: x[1]))
ch = 0
for l in letters:
    letters[l] += ch
    ch += letters[l] - ch

def get_letter() -> str:
    i = random.randint(len(text) // 2, len(text))
    for l in letters:
        if letters[l] > i: return l

result = "".join([get_letter() for _ in range(100)]).replace(" ", "")
print(result)