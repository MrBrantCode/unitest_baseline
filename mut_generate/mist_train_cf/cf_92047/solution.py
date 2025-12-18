"""
QUESTION:
Create a function `count_words_and_numbers` that takes a list of strings as input where the strings are either words or numbers. The function should return or print the unique words, unique numbers, and the frequency of each unique word. The input list can contain duplicate words and numbers.
"""

def count_words_and_numbers(input_list):
    unique_words = set()
    unique_numbers = set()
    word_frequency = {}

    for item in input_list:
        if item.isnumeric():
            unique_numbers.add(item)
        else:
            unique_words.add(item)
            if item in word_frequency:
                word_frequency[item] += 1
            else:
                word_frequency[item] = 1

    return unique_words, unique_numbers, word_frequency