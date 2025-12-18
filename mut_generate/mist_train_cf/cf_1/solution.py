"""
QUESTION:
Write a function `count_distinct_states(matrix)` to find the number of distinct states in a given matrix. Each state in the matrix can be represented by a string of characters. The function should have a time complexity of O(N), where N is the total number of characters in the matrix.
"""

def count_distinct_states(matrix):
    """
    This function counts the number of distinct states in a given matrix.
    
    Args:
    matrix (list): A 2D list of characters where each sub-list represents a row in the matrix.
    
    Returns:
    int: The number of distinct states in the matrix.
    """
    distinct_states = set()
    for row in matrix:
        for col in row:
            state = ''.join(map(str, col))
            distinct_states.add(state)
    return len(distinct_states)