"""
QUESTION:
Write a function named `highest_binary_value` that takes two parameters: an unordered list of distinct binary strings `arr` and an integer `n`. The function should return the nth highest binary string value in the list. The function should convert the binary strings to integers for comparison, then convert the result back to a binary string. Assume 1 <= n <= length of array.
"""

def highest_binary_value(arr, n):
    # convert binary strings to integers
    arr_nums = [int(num, 2) for num in arr]

    # sort the list in descending order
    arr_nums.sort(reverse=True)

    # get the nth highest value and convert back to binary string
    nth_highest = bin(arr_nums[n-1])[2:]

    return nth_highest