"""
QUESTION:
Write a function called `find_modes` that takes a list of integers as input and returns a list of modes in ascending order. The mode is the number that appears most frequently in the list. If there are multiple numbers that appear the same maximum number of times, the function should return a list of all the modes. The function should have a time complexity of O(n) and should be able to handle empty lists and lists containing both positive and negative integers.
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