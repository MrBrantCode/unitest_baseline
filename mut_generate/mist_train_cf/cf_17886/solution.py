"""
QUESTION:
Write a function named `find_largest_palindrome` that takes an array of integers as input and returns the index of the largest palindromic number in the array. The function should return the index of the first occurrence if there are multiple palindromic numbers with the same maximum length. If there are no palindromic numbers in the array, the function should return -1. The time complexity should be O(n) and constant space should be used.
"""

def find_largest_palindrome(arr):
    max_length = -1
    max_index = -1

    for i in range(len(arr)):
        num = str(arr[i])
        if num == num[::-1] and len(num) > max_length:
            max_length = len(num)
            max_index = i

    return max_index