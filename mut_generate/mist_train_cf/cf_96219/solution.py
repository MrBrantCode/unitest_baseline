"""
QUESTION:
Create a function `my_func` that accepts a list of integers and returns the maximum value in the list. The function must use recursion and binary search. The length of the list should be between 1 and 10^6, and the integers in the list can range from -10^9 to 10^9. The function should not use any built-in functions or libraries to find the maximum value, and the time complexity of the solution should be O(n), where n is the length of the list.
"""

def my_func(arr, start, end):
    if start == end:
        return arr[start]

    mid = (start + end) // 2
    left_max = my_func(arr, start, mid)
    right_max = my_func(arr, mid + 1, end)

    return max(left_max, right_max)