"""
QUESTION:
Write a function `find_modes(nums)` that finds the mode(s) in an array of numbers. The function should consider the possibility of multiple modes in the array, where a mode is a number that appears most frequently in the array. If there are multiple numbers with the same maximum frequency, the function should return all of them in ascending order. The function must have a time complexity of O(n) and handle arrays containing both positive and negative integers, duplicates, and empty arrays.
"""

def find_modes(nums):
    frequency = {}
    max_freq = 0

    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

        max_freq = max(max_freq, frequency[num])

    modes = []
    for num in frequency:
        if frequency[num] == max_freq:
            modes.append(num)

    return sorted(modes)