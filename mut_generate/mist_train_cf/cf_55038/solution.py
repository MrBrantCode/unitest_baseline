"""
QUESTION:
Write a function called `recursive_reverse` that takes a single list `arr` as input and returns the reversed list. The function must use recursion and can only use list slicing and concatenation to reverse the list. 

The function should be able to handle an empty list and should not modify the original list. Additionally, write a function `reverse_all` that takes a list of lists as input and returns a new list where each inner list is reversed using the `recursive_reverse` function.
"""

def recursive_reverse(arr):
    if len(arr) == 0:
        return arr
    else:
        return recursive_reverse(arr[1:]) + [arr[0]]

def reverse_all(arr):
    return [recursive_reverse(sub_array) for sub_array in arr]