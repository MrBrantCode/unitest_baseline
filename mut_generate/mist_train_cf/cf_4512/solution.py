"""
QUESTION:
Implement a function named `most_frequent_element` that takes a list of integers as input and returns the element that appears most frequently, considering only elements that appear at least three times. The input list will contain at most 10^6 elements, and each element will be an integer between -10^9 and 10^9. You are not allowed to use any built-in sorting or counting functions in your solution.
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