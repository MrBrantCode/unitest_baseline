"""
QUESTION:
Write a function `second_most_common_element(lst)` that finds the second most common element in a list, considering only elements that appear at least twice. The function should handle lists containing negative numbers and have a time complexity of O(n), where n is the length of the list.
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
        if frequency == second_highest_freq and frequency > 1:
            return element

    # Return None if there is no second most common element
    return None