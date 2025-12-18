"""
QUESTION:
Write a function named `calculate_word_frequencies` and `print_word_frequencies` to calculate and print the frequency of each word in the input dictionary. The frequency of each word should be represented as a percentage of the total number of words in the dictionary, rounded to the nearest whole number. The code should handle input dictionaries with up to 100 million words efficiently, use as little memory as possible, and treat words with different cases as distinct words. The implementation should only use built-in Python functions and avoid using any external libraries or modules. The words should be printed in descending order of their frequency, and if two or more words have the same frequency, they should be sorted alphabetically.
"""

def calculate_word_frequencies(dictionary):
    total_words = sum(dictionary.values())
    frequencies = {word: (count / total_words) * 100 for word, count in dictionary.items()}
    return frequencies


def print_word_frequencies(dictionary):
    frequencies = calculate_word_frequencies(dictionary)

    sorted_words = sorted(frequencies.keys(), key=lambda x: (-frequencies[x], x))
    for word in sorted_words:
        print(f"{word}: {round(frequencies[word])}% ({dictionary[word]} occurrences)")