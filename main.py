from writeFile import write_file
from readFile import read_file, return_dictionary, return_starting_words
from generateHeadline import generate_headline


# change to write new headlines.txt file
def main_func():
    new_file = False

    if new_file:
        write_file()

    read_file()

    starting_words = return_starting_words()

    markov_dictionary = return_dictionary()

    return generate_headline(starting_words, markov_dictionary)
