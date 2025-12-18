"""
QUESTION:
Create a list comprehension function `filter_pairs` that takes a list of tuples as input and returns a new list containing only the tuples where the first element is a palindrome string and the second element is a prime number. The list of tuples contains string and integer pairs.
"""

def filter_pairs(my_list):
    """
    This function filters a list of tuples to include only the tuples 
    where the first element is a palindrome string and the second element is a prime number.

    Args:
        my_list (list): A list of tuples containing string and integer pairs.

    Returns:
        list: A new list containing the filtered tuples.
    """
    return [pair for pair in my_list if pair[0] == pair[0][::-1] and all(pair[1] % i != 0 for i in range(2, int(pair[1]**0.5) + 1))]