"""
QUESTION:
Create a function named `numerical_sort(n, key)` that takes a string of numbers `n` and a key number `key` as input. The string of numbers may contain commas, spaces, or both as separators. The function should extract the numbers into a list, remove the key number, invert the list, and then return a sorted list containing only numbers less than or equal to 70.
"""

def numerical_sort(n, key):
    # Extract numbers into a list by splitting the string by comma and space
    num_list = [int(num) for num in n.replace(",", " ").split()]
    # Ignore instances of key number
    num_list = [num for num in num_list if num != key]
    # Invert the sequence of the remaining numbers
    num_list.reverse()
    # Return the list following a numerical sort and ignore any number that is greater than 70
    return sorted([num for num in num_list if num <= 70])