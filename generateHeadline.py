import random


def add_to_sentence(sentence, word):
    sentence = sentence + " " + word + " "
    return sentence


def next_word(currWord, dictionary):
    if currWord in dictionary.keys():
        return random.choice(dictionary[currWord])
    return None


def generate_headline(startingWords, dictionary):
    sentence = ""
    # generate a random starting word
    current = random.choice(startingWords)
    while current is not None:
        sentence = add_to_sentence(sentence, current)
        current = next_word(current, dictionary)
    return sentence
