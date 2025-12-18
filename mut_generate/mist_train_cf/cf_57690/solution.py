"""
QUESTION:
Write a function `count_freq` that takes an array of integers as input and returns a dictionary where the keys are the unique integers from the array and the values are their corresponding frequencies. Implement this function without using built-in functions like `collections.Counter`. Additionally, write a function `sort_freq_dict` that takes the resulting dictionary and returns a new dictionary sorted by its values in descending order.
"""

def count_freq(arr):
    freq_dict = {}
    for num in arr:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    return freq_dict

def sort_freq_dict(freq_dict):
    sorted_dict = {k: v for k, v in sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)}
    return sorted_dict