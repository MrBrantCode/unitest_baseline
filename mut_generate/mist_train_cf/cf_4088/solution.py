"""
QUESTION:
Write a function called `second_most_common_element` that takes a list of integers as input, finds the element that appears the second most frequently in the list, and returns this element. The input list may contain duplicates, negative numbers, and the second most common element must appear at least twice. The function should have a time complexity of O(n), where n is the length of the list. If no such element exists, the function should return `None`.
"""

def second_most_common_element(lst):
    # Create a dictionary to store the frequency of each element
    freq = {}
    for element in lst:
        if element in freq:
            freq[element] += 1
        else:
            freq[element] = 1

    # Find the second highest frequency
    highest_freq = 0
    second_highest_freq = 0
    for element, frequency in freq.items():
        if frequency > highest_freq:
            second_highest_freq = highest_freq
            highest_freq = frequency
        elif frequency > second_highest_freq and frequency < highest_freq:
            second_highest_freq = frequency

    # Find the element corresponding to the second highest frequency
    for element, frequency in freq.items():
        if frequency == second_highest_freq and second_highest_freq > 1:
            return element

    # Return None if there is no second most common element
    return None