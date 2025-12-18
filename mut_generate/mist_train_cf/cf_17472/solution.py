"""
QUESTION:
Create a function `sort_array` that takes an array of integers as input. Sort the array based on the frequency of occurrence of each integer in descending order. If multiple integers have the same frequency, sort them in descending order. The function should return the sorted array.
"""

def sort_array(arr):
    # Create a dictionary to store the frequency of each integer in the array
    freq_dict = {}
    for num in arr:
        freq_dict[num] = freq_dict.get(num, 0) + 1

    # Sort the array based on the frequency count in descending order
    arr.sort(key=lambda x: (-freq_dict[x], -x))

    return arr