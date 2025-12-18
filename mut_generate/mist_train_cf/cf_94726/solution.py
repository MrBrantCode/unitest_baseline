"""
QUESTION:
Create a function named `sort_array` that takes an array of integers as input and returns the array sorted based on the frequency of occurrence of each integer. If multiple integers have the same frequency, they should be sorted in descending order.
"""

def sort_array(arr):
    # Step 1: Create a dictionary to store the frequency of each integer in the array
    freq_dict = {}
    for num in arr:
        freq_dict[num] = freq_dict.get(num, 0) + 1

    # Step 2: Sort the array based on the frequency count in descending order
    arr.sort(key=lambda x: (-freq_dict[x], -x))

    return arr