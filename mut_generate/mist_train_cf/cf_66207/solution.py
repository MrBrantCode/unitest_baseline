"""
QUESTION:
Create a function called `count_letters(matrix)` that takes a 2D array (matrix) of single character strings as input and returns a dictionary containing the count of each alphabetic symbol in the matrix, ignoring case and non-alphabetic characters. The matrix elements can be either lowercase or uppercase letters, and the function should treat them as the same letter. The function should not count non-alphabetic characters.
"""

def count_letters(matrix):
    letter_counts = {}
    for row in matrix:
        for char in row:
            if char.isalpha():
                char = char.lower()
                if char not in letter_counts:
                    letter_counts[char] = 1
                else:
                    letter_counts[char] += 1
    return letter_counts