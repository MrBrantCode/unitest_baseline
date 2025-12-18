"""
QUESTION:
Write a function `count_distinct_states(matrix)` to find the number of distinct states in a given matrix, where each state can be represented by a string of characters. The function should have a time complexity of O(N), where N is the total number of characters in the matrix. The input matrix is a 2D list of characters, and the function should return the count of distinct states.
"""

def count_distinct_states(matrix):
    states = set()
    for row in matrix:
        for col in row:
            state = ''.join(map(str, col))
            states.add(state)
    return len(states)