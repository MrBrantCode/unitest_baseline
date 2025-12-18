"""
QUESTION:
Write a function called `reverse_strings` that takes an array of strings as input and returns a new array with each string reversed. The function should not use any built-in string reverse methods. The input array may contain any number of strings, and the function should return a new array with the same number of strings, each of which is the reverse of the corresponding string in the input array.
"""

def reverse_strings(arr):
    """
    This function takes an array of strings as input and returns a new array with each string reversed.
    
    Parameters:
    arr (list): A list of strings
    
    Returns:
    list: A new list with each string reversed
    """
    reversed_array = []
    for string in arr:
        reversed_string = ''
        for char in range(len(string) - 1, -1, -1):
            reversed_string += string[char]
        reversed_array.append(reversed_string)
    return reversed_array