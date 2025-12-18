"""
QUESTION:
Write a function `find_uneven_frequency` that takes a 2D array of integers as input and returns the first integer that appears with an uneven frequency during the traversal of the array. The function should have a time complexity of O(n), where n is the total number of elements in the 2D array. If no such integer is found, return None. The input 2D array may not be square, i.e., the number of rows may not be equal to the number of columns.
"""

def find_uneven_frequency(arr):
    frequency_dict = {}

    for sublist in arr:
        for num in sublist:
            frequency_dict[num] = frequency_dict.get(num, 0) + 1
            if frequency_dict[num] % 2 != 0:  # uneven frequency
                return num

    return None  # if no such integer is found