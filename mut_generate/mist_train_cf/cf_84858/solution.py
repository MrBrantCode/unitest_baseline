"""
QUESTION:
Write a function `count_occurrences` that takes a two-dimensional array of integers as input and returns a list of tuples. Each tuple should contain a unique integer from the array and its frequency. The list should be sorted in descending order of frequency. The function should handle arrays with rows of different sizes and should work with negative integers.
"""

def count_occurrences(two_d_array):
    count_dict = {}
    for lst in two_d_array:
        for item in lst:
            if item not in count_dict:
                count_dict[item] = 1
            else:
                count_dict[item] += 1
    return sorted(count_dict.items(), key=lambda x: x[1], reverse=True)