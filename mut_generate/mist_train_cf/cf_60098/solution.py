"""
QUESTION:
Create a function called `count_letters` that takes a string `text` as input and returns a list of tuples. The function should ignore case sensitivity and special characters, count the frequency of each letter in the string, and return the frequency count in descending order. The output should be a list of tuples where each tuple contains a letter and its frequency.
"""

from collections import Counter
import re

def count_letters(text):
    # Convert the text to lowercase and remove all non-letter characters.
    text = re.sub("[^a-z]", "", text.lower())

    # Count the frequency of each letter using collections.Counter.
    letter_freq = Counter(text)

    # Return the letter frequencies in descending order.
    return sorted(letter_freq.items(), key=lambda x: x[1], reverse=True)