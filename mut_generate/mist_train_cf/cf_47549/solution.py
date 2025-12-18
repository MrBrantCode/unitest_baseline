"""
QUESTION:
Write a function `solve` that takes a list of strings as input, removes duplicates, counts the occurrences of each word, sorts the words in descending order based on the count of their occurrences and then lexicographically for words with the same count, and returns or prints the modified list and the count of occurrences for each word in the sorted list.
"""

from collections import Counter

def solve(strings):
    count = Counter(strings)
    modified_list = sorted(count.items(), key=lambda x: (-x[1], x[0]))
    return modified_list