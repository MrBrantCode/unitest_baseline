"""
QUESTION:
Write a function named `find_second_most_frequent` that takes an array of integers as input and returns a list of the second most frequent elements. If there are multiple elements with the same second highest frequency, all of them should be included in the output list. The input array can contain duplicate elements.
"""

def find_second_most_frequent(arr):
    freq_map = {}
    for num in arr:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1
    
    max_freq = -1
    second_max_freq = -1
    for num, freq in freq_map.items():
        if freq > max_freq:
            second_max_freq = max_freq
            max_freq = freq
        elif freq > second_max_freq and freq < max_freq:
            second_max_freq = freq
    
    second_most_frequent = []
    for num, freq in freq_map.items():
        if freq == second_max_freq:
            second_most_frequent.append(num)
    
    return second_most_frequent