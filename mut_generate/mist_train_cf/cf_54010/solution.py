"""
QUESTION:
Write a function `smallestChange` that takes a list of integers `arr` as input and returns the minimum number of transformations required to make the array a palindrome. A transformation consists of incrementing or decrementing an integer by 1. Once an integer reaches its target value, it can't be changed again. Negative integers are allowed.
"""

def smallestChange(arr):
    """
    This function calculates the minimum number of transformations required to make the array a palindrome.
    A transformation consists of incrementing or decrementing an integer by 1.
    Once an integer reaches its target value, it can't be changed again. Negative integers are allowed.

    Parameters:
    arr (list): A list of integers.

    Returns:
    int: The minimum number of transformations required to make the array a palindrome.
    """
    changes = 0

    i = 0
    j = len(arr) - 1
    while i <= j:
        if arr[i] != arr[j]:
            changes += abs(arr[i] - arr[j])
        i += 1
        j -= 1

    return changes