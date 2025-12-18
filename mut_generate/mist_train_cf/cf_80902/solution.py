"""
QUESTION:
Implement a function `closest_match(input_string: str, word_list: list) -> Tuple[str, int]` that finds the closest match of `input_string` from a given list of words `word_list` using the Levenshtein edit distance. The function should return a tuple containing the closest match and the minimum edit distance value. The implementation should handle variations in string length and character repetitions, and be time and space efficient.
"""

import sys
from typing import List, Tuple

def closest_match(input_string: str, word_list: List[str]) -> Tuple[str, int]:
    def compute_levenshtein_distance(str1: str, str2: str) -> int:
        matrix = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
        
        for i in range(len(str1) + 1):
            matrix[i][0] = i
        for j in range(len(str2) + 1):
            matrix[0][j] = j
        
        for i in range(1, len(str1) + 1):
            for j in range(1, len(str2) + 1):
                if str1[i-1] == str2[j-1]:
                    substitution_cost = 0
                else:
                    substitution_cost = 1

                matrix[i][j] = min(matrix[i-1][j] + 1,      # deletion
                                    matrix[i][j-1] + 1,      # insertion
                                    matrix[i-1][j-1] + substitution_cost) # substitution
        
        return matrix[len(str1)][len(str2)]

    closest_word = ""
    minimum_distance = sys.maxsize

    for word in word_list:
        distance = compute_levenshtein_distance(input_string, word)
        if distance < minimum_distance:
            minimum_distance = distance
            closest_word = word
    return closest_word, minimum_distance