"""
QUESTION:
Develop a function named `most_frequent` that takes an array of elements as input and returns a list of tuples, where each tuple contains an element and its frequency. The function should return all elements with the highest frequency. The function should handle an empty input array and return an empty list. The solution should be optimized for both time and space complexity.
"""

def most_frequent(arr):
    if not arr:
        return []
    element_freq = {}
    max_freq = 0
    for element in arr:
        if element not in element_freq:
            element_freq[element] = 1
        else:
            element_freq[element] += 1
        if element_freq[element] > max_freq:
            max_freq = element_freq[element]

    result = [(e, freq) for e, freq in element_freq.items() if freq == max_freq]
    return result