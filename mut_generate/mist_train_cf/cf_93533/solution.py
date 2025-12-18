"""
QUESTION:
Write a function `count_distinct_states` that takes a 2D list `matrix` as input where each element in the matrix is a character. The function should return the number of distinct states in the matrix where each state is represented by a string of characters in a row. The matrix can have up to 10^6 rows and columns.
"""

def count_distinct_states(matrix):
    count = 0
    states = set()
    for row in matrix:
        state = ''.join(row)
        if state not in states:
            count += 1
        states.add(state)
    return count