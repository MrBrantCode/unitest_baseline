"""
QUESTION:
Create a function called `calculate_word_frequencies` that calculates the frequency of each word in the input dictionary as a percentage of the total number of words. The function should handle input dictionaries with up to 100 million words efficiently, use as little memory as possible, and treat words in a case-sensitive manner. The function should return a dictionary where the keys are the words and the values are the corresponding frequencies as percentages rounded to the nearest whole number. Implement the function using only built-in Python functions and avoid using any external libraries or modules.

Create another function called `print_word_frequencies` that takes the input dictionary, calculates the word frequencies using the `calculate_word_frequencies` function, sorts the words in descending order of their frequency, and then alphabetically for words with the same frequency, and prints out the words along with their frequencies and occurrences.
"""

def calculate_word_frequencies(dictionary):
    total_words = sum(dictionary.values())
    frequencies = {word: (count / total_words) * 100 for word, count in dictionary.items()}
    return {word: round(frequency) for word, frequency in frequencies.items()}


def print_word_frequencies(dictionary):
    frequencies = calculate_word_frequencies(dictionary)
    sorted_words = sorted(frequencies.keys(), key=lambda x: (-frequencies[x], x))
    for word in sorted_words:
        print(f"{word}: {frequencies[word]}% ({dictionary[word]} occurrences)")