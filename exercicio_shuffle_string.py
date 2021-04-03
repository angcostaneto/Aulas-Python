from random import sample, randint


def shuffle_easy(text):
    text = sample(text, len(text))
    response = ""
    for i in range(len(text)):
        response += text[i]

    return response


def shuffle_hard(text):
    length = len(text)
    text = list(text)

    for letter_position in range(0, length - 1):
        new_position = randint(letter_position + 1, length - 1)
        text[new_position], text[letter_position] = text[letter_position], text[new_position]

    response = ''
    for i in range(length):
        response += text[i]

    return response


print(shuffle_easy('python'))
print(shuffle_hard('python'))
