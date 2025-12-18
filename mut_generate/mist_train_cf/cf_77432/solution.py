"""
QUESTION:
Design a function named `count_chars` that takes a list of strings `lexemes` as input and calculates the statistical occurrence rate of distinct alphabetic characters within the strings. The function should ignore non-alphabetic characters, be case sensitive, and output the occurrence rate of each distinct alphabetic character as a percentage.
"""

from collections import Counter
import string

def count_chars(lexemes):
    # join all lexemes into a single string
    all_chars = ''.join(lexemes)
    
    # filter out non-alphabetic characters and count occurrences
    counts = Counter(ch for ch in all_chars if ch in string.ascii_letters)
    
    # calculate the total number of alphabetic characters
    total = sum(counts.values())
    
    # calculate and return occurrence rates
    return {char: count / total * 100 for char, count in counts.items()}