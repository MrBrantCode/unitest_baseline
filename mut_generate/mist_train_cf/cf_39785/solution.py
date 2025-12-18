"""
QUESTION:
Create a function `calculate_freq_times(arr)` that takes a list of elements as input and returns a new list containing the product of each element with its frequency in the input list. The function should return a list of products in any order, as long as each product corresponds to an element in the input list.
"""

def calculate_freq_times(arr):
    freq_dict = {}
    for num in arr:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    
    freqtimes = [num * freq_dict[num] for num in set(arr)]
    return freqtimes