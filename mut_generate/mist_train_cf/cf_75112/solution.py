"""
QUESTION:
Create a function named `is_descending_alphabetical_order` that takes an array of strings as input. The function should return True if the array is in descending alphabetical order and False otherwise. The function must use comparison operators and iterative loops. The input array contains only strings.
"""

def is_descending_alphabetical_order(arr):
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            return False
    return True