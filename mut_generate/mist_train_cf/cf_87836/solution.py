"""
QUESTION:
Write a function named `is_palindrome` that takes an array as input and returns `True` if the array is a palindrome and `False` otherwise. The palindrome condition is defined as follows: if the array has an odd length, the middle element can be any value; if the array has an even length, all elements must be the same value; the array must be read the same forward and backward, ignoring any non-alphanumeric characters and case sensitivity. The function must have a time complexity of O(n), where n is the length of the array, and must not use any built-in functions or libraries that directly solve the problem.
"""

def is_palindrome(arr):
    cleaned_arr = [str(elem).lower() for elem in arr if str(elem).isalnum()]
    length = len(cleaned_arr)
    if length % 2 == 1:
        middle_index = length // 2
        left = cleaned_arr[:middle_index]
        right = cleaned_arr[middle_index + 1:]
    else:
        left = cleaned_arr[:length // 2]
        right = cleaned_arr[length // 2:]
    return left == right[::-1] and (length % 2 == 1 or all(elem == left[0] for elem in left))