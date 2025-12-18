"""
QUESTION:
Write a function named count_distinct_states that takes a 2D list of strings (matrix) as input and returns the number of distinct states. Each state is represented by a string of characters in a row of the matrix. The function should be able to handle matrices with up to 10^6 rows and columns.
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