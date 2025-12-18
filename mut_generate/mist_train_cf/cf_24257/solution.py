"""
QUESTION:
Write a function `largest_palindromic_number(arr)` that finds the largest palindromic number in a given array of integers. A palindromic number reads the same backward as forward. The function should return the largest palindromic number in the array. If no palindromic number exists, the function should return 0.
"""

def largest_palindromic_number(arr):
    largest = 0

    for i in arr:
        s = str(i)
        if s == s[::-1]:
            largest = max(i, largest) 
    return largest