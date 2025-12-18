"""
QUESTION:
Write a function `largest_palindromic_number(arr)` that finds the largest palindromic number in a given array and returns its index. If there are multiple palindromic numbers with the same maximum length, return the index of the first occurrence. If there are no palindromic numbers in the array, return -1. The array can contain both positive and negative integers, with a maximum of 10^6 elements and each integer having a maximum of 9 digits.
"""

def largest_palindromic_number(arr):
    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    max_length = -1
    max_index = -1

    for i in range(len(arr)):
        if is_palindrome(arr[i]):
            length = len(str(arr[i]))
            if length > max_length:
                max_length = length
                max_index = i

    return max_index