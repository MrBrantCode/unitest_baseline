"""
QUESTION:
Write a function `is_palindrome` to determine whether a given array of elements is a palindrome, considering the order and type of elements. The function should handle arrays containing integers, floating point numbers, strings, nested arrays or complex data structures, null or undefined values, and objects or custom data types. It should return `True` only if the array remains the same when reversed. The implementation should have a time complexity of O(n), where n is the length of the array, and should not use any built-in reverse functions or methods to reverse the array.
"""

def is_palindrome(arr):
    def compare_elements(a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a == b
        if isinstance(a, str) and isinstance(b, str):
            return a == b
        if isinstance(a, type(b)) or isinstance(b, type(a)):
            return a == b
        return False

    def is_palindrome_recursive(arr, start, end):
        if start >= end:
            return True
        
        first = arr[start]
        last = arr[end]
        
        if not compare_elements(first, last):
            return False
        
        return is_palindrome_recursive(arr, start + 1, end - 1)

    return is_palindrome_recursive(arr, 0, len(arr) - 1)