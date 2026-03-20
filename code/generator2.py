import random

def get_data(filepath: str) -> str:
    with open(filepath, "r") as f: return f.read()

def get_tokens(token_lenght: int, text: str, alphabet: list | None = None) -> dict:
    if alphabet == None: alphabet = sorted(set(text))

    tokens = dict()    # { token: { letter of the alphabet: count, ... } }
    for i in range(len(text) - token_lenght - 1):
        token = text[i : i + token_lenght]
        if token not in tokens:
            tokens[token] = dict()
            for letter in alphabet:
                tokens[token][letter] = 0
            tokens[token][text[i + token_lenght]] += 1
        else:
            tokens[token][text[i + token_lenght]] += 1
    
    for t in tokens:
        tokens[t] = dict(sorted(
            tokens[t].items(),
            key=lambda x: x[1]
        ))
    
    ch = 0
    for t in tokens:
        for l in tokens[t]:
            tokens[t][l] += ch
            ch += tokens[t][l] - ch
        ch = 0
    
    return tokens

def get_next_letter(token_letters: dict) -> str:
    max_value = list(token_letters.items())[-1][1]
    i = random.randint(max_value // 2, max_value - 1)
    for l in token_letters:
        if token_letters[l] > i: return l
    return random.choice(list(token_letters.items()))[0]

def generate_text(lenght: int, token: str, text_data: str) -> str:
    result = token
    tokens = get_tokens(len(token), text_data)
    
    for _ in range(lenght):
        new_letter = ""
        for _ in token:
            try:
                new_letter = get_next_letter(tokens[token])
                break
            except KeyError:
                token = token[1:]
                tokens = get_tokens(len(token), text_data)
        if not new_letter: return result

        token = token[1:] + new_letter
        result += new_letter

    return result


RECOMMENDED_EXTRA_CHARS = [
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
    '!', ',', '.', '?', '<', '>', '[', ']', '/', '-',
    '@', '^', '&', ':', ';', '`', '~', '=', '+', '*',
    '{', '}', 'xxx', 'xviii', 'xvii', 'vii', 'lxii', 'liii', '\'', '"'
]

def remove_extra_chars(text_data: str, extra_chars) -> str:
    if extra_chars:
        for char in extra_chars: text_data = text_data.replace(char, '')
    
    text_data = text_data.replace("\n", " ")
    result = ""
    prev_whitespace = False
    for char in text_data:
        if char == ' ':
            if prev_whitespace: continue
            else: prev_whitespace = True
        else: prev_whitespace = False
        
        result += char

    return result


# EXAMPLE

filepath1 = "/home/alexey/IT/Experiment_text_generator/data/EugeneOnegin.txt"
filepath2 = "/home/alexey/IT/Experiment_text_generator/data/SherlockHolmes.txt"

text_data = remove_extra_chars(get_data(filepath1).lower(), RECOMMENDED_EXTRA_CHARS) \
    + f" {remove_extra_chars(get_data(filepath2).lower(), RECOMMENDED_EXTRA_CHARS)}"

input_word = remove_extra_chars(input("Enter word: "), RECOMMENDED_EXTRA_CHARS)
print(generate_text(100, input_word, text_data))