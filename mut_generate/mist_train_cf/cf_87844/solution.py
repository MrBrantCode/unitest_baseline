"""
QUESTION:
Write a function named `sort_data` that sorts a list of tuples in descending order based on the following criteria: 
1. The score (second element of the tuple) in descending order.
2. If scores are the same, by the name (first element of the tuple) in descending order of ASCII values.
3. If scores and names are the same, by the ID number (third element of the tuple) in descending order. 

The function should take a list of tuples as input, where each tuple contains a name (string), a score (integer), and an ID number (integer).
"""

def sort_data(data):
    """
    Sorts a list of tuples in descending order based on the score, name, and ID number.

    Args:
        data (list): A list of tuples, where each tuple contains a name (string), a score (integer), and an ID number (integer).

    Returns:
        list: The sorted list of tuples.
    """
    return sorted(data, key=lambda x: (-x[1], -ord(x[0][0]), -x[2]))