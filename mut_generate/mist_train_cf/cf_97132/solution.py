"""
QUESTION:
Write a function `most_frequent_element` that takes a list of integers as input, where the list length is at least 10 and may contain negative numbers, and returns the element that occurs most frequently in the list. The function should have a time complexity of O(n), where n is the length of the list.
"""

def most_frequent_element(lst):
    freq_count = {}
    max_freq = 0
    most_freq_element = None

    for num in lst:
        if num not in freq_count:
            freq_count[num] = 1
        else:
            freq_count[num] += 1

        if freq_count[num] > max_freq:
            max_freq = freq_count[num]
            most_freq_element = num

    return most_freq_element