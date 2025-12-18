"""
QUESTION:
Write a function called `recursive_reverse` that uses a recursive algorithm to reverse the order of elements in a given list. The function should take two parameters: the list to be reversed and the length of the list. Do not use any built-in list reversal functions.
"""

def recursive_reverse(arr, length):
    if length == 0:
        return

    recursive_reverse(arr, length - 1)
    arr.append(arr[length - 1])
    arr.pop(length - 1)