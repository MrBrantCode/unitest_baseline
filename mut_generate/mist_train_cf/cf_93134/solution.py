"""
QUESTION:
Find the three largest numbers in the given array of integers and return them in descending order. The function `find_three_highest_numbers` should achieve this with a time complexity of O(n log n) and constant space complexity. The input array contains at most 10^5 integers, ranging from -10^9 to 10^9.
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