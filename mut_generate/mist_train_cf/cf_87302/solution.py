"""
QUESTION:
Write a function called `is_palindrome` to determine whether an array containing integers, floating point numbers, and strings is a palindrome. The function should handle arrays with negative integers and floating point numbers, and consider the order and type of elements. It should return True only if the array remains the same when its elements are reversed. The function should have a time complexity of O(n) and should not use any built-in reverse functions or methods.
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