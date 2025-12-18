"""
QUESTION:
Write a function called `select_letters` that takes two arguments: an array of letters and the number of letters to select. The function should return all possible combinations of the given length from the array of letters. The combinations should be returned as a list of strings, with each string representing a combination of letters.
"""

from itertools import combinations

def select_letters(arr, num):
    return [''.join(tup) for tup in combinations(arr, num)]