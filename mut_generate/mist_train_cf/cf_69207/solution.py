"""
QUESTION:
Develop a function `recursive_sum` that takes a list of strings representing numbers and returns the sum of the numbers using recursion. The function should attempt to convert each string to an integer, and if successful, include it in the sum. If a string cannot be converted to an integer, the function should return an error message. The function should start at the first element of the list by default, and should be able to handle lists of varying lengths.
"""

def recursive_sum(lst, index=0):
    # base case: if index is out of bounds, return 0
    if index == len(lst):
        return 0
    
    try:
        # attempt to convert the current element to an integer
        number = int(lst[index])
    except ValueError:
        return "Error: could not convert '{}' to integer.".format(lst[index])

    # add current number to the sum of remaining numbers
    return number + recursive_sum(lst, index + 1)