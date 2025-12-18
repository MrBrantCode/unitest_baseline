"""
QUESTION:
Write a function `largest_palindromic_number` that takes an array of integers as input and returns the index of the largest palindromic number in the array. If there are multiple palindromic numbers with the same maximum length, return the index of the first occurrence. If there are no palindromic numbers in the array, return -1. The array can contain both positive and negative integers, with a maximum length of 9 digits per number and a maximum of 10^6 elements in the array.
"""

def largest_palindromic_number(arr):
    max_length = -1
    max_index = -1

    for i in range(len(arr)):
        if str(arr[i]) == str(arr[i])[::-1]:
            length = len(str(arr[i]))
            if length > max_length:
                max_length = length
                max_index = i

    return max_index