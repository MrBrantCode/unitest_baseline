"""
QUESTION:
Write a function called `convert_and_sort` that takes an array of strings as input, converts the numeric strings to integers, excludes non-numeric strings, and returns the converted integers in a new array sorted in descending order. The function should not use any built-in sorting functions or libraries.
"""

def convert_and_sort(arr):
    converted_nums = []
    for num in arr:
        try:
            converted_nums.append(int(num))
        except ValueError:
            continue

    # Bubble sort in descending order
    n = len(converted_nums)
    for i in range(n):
        for j in range(0, n-i-1):
            if converted_nums[j] < converted_nums[j+1]:
                converted_nums[j], converted_nums[j+1] = converted_nums[j+1], converted_nums[j]

    return converted_nums