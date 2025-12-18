"""
QUESTION:
Design a function `calculate_frequency_ratio(phrases)` that calculates the frequency ratio of alphanumeric terms within an array of strings. The function should extract alphanumeric terms from each string in the input list, count their occurrences, and return a dictionary where keys are the alphanumeric terms and values are their corresponding frequency ratios. The frequency ratio is calculated as the count of each term divided by the total count of all terms. The function should treat alphanumeric terms case-sensitively and consider terms separated by non-alphanumeric characters as distinct terms.
"""

from collections import Counter
import re

def calculate_frequency_ratio(phrases):
    counter = Counter()
    for phrase in phrases:
        words = re.findall(r'\b\w+\b', phrase)
        counter.update(words)
    total_words = sum(counter.values())
    frequencies = {word: count/total_words for word, count in counter.items()}
    return frequencies