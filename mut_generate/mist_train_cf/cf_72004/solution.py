"""
QUESTION:
Create a function `letter_counter(matrix)` that takes a 2D list `matrix` as input and returns a dictionary where the keys are the unique alphabetic symbols in the matrix (case-insensitive) and the values are their respective counts. The function should only consider alphabetic symbols and ignore any other characters.
"""

def letter_counter(matrix):
    # Create a dictionary to store alphabetic symbols counts
    symbols_counts = {}

    # Iterate over the elements in matrix and update count
    for row in matrix:
        for element in row:
            # Only process elements if they are alphabetic symbol
            if element.isalpha():
                element = element.lower()  # handling case-insensitive symbols
                symbols_counts[element] = symbols_counts.get(element, 0) + 1

    return symbols_counts