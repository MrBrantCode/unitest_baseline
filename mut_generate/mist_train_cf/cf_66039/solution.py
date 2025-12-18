"""
QUESTION:
Create a function `eliminate_nums` that takes an array of integers as input. The function should remove any integer that occurs more than three times in the array and return the remaining integers in descending order without using any built-in sort functions.
"""

def eliminate_nums(arr):
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    unique_nums = [num for num in frequency if frequency[num] <= 3]

    for i in range(len(unique_nums)):
        for j in range(i+1, len(unique_nums)):
            if unique_nums[i] < unique_nums[j]:
                unique_nums[i], unique_nums[j] = unique_nums[j], unique_nums[i]

    return unique_nums