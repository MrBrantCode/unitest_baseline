"""
QUESTION:
Write a function `get_mode_complex_array(arr)` that finds the mode in an array of complex numbers. The mode is the complex number that appears most frequently in the array. If there are multiple modes (i.e., two or more complex numbers appear the same highest number of times), the function should return one of them. The function should not use any external libraries.
"""

def get_mode_complex_array(arr):
    frequency_dict = {}
    for num in arr:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1
    mode = max(frequency_dict, key=frequency_dict.get)
    return mode