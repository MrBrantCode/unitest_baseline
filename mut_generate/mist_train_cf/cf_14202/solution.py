"""
QUESTION:
Write a function `find_three_highest_numbers(arr)` that takes an array of integers as input and returns the three largest numbers in descending order. The input array contains at most 10^5 integers, ranging from -10^9 to 10^9. The function should have a time complexity of O(n) and use constant space.
"""

def find_three_highest_numbers(arr):
    first = second = third = float('-inf')
    for num in arr:
        if num > first:
            third = second
            second = first
            first = num
        elif num > second:
            third = second
            second = num
        elif num > third:
            third = num
    return [first, second, third]