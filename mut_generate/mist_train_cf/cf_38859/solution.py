"""
QUESTION:
Write a function `find_first_pair_indices(sentence: str)` that takes a string `sentence` as input. The function should return a tuple of two integers representing the 1-based ordinal numbers of the first pair of adjacent identical characters in the input sentence. If no such pair exists, the function should return the string "No matching pair found". The input sentence may contain printable ASCII characters, including spaces and punctuation.
"""

from typing import Union, Tuple

def find_first_pair_indices(sentence: str) -> Union[Tuple[int, int], str]:
    for ind in range(len(sentence) - 1):
        if sentence[ind] == sentence[ind + 1]:
            return (ind + 1, ind + 2)
    return "No matching pair found"