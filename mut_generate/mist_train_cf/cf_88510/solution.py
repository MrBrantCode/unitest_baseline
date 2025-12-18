"""
QUESTION:
Implement a function called `most_frequent_element` that takes a list of integers as input and returns the integer that appears most frequently, considering only integers that appear at least three times. The input list may contain up to 10^6 elements, and each element is an integer between -10^9 and 10^9. The function should not use any built-in sorting or counting functions.
"""

def most_frequent_element(lst):
    frequency = {}
    for num in lst:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    most_frequent = None
    max_frequency = 0
    for num, count in frequency.items():
        if count >= 3 and count > max_frequency:
            most_frequent = num
            max_frequency = count

    return most_frequent