"""
QUESTION:
Construct a function `construct_dictionary(key_arr, value_arr)` that takes two input arrays: `key_arr` and `value_arr`, where `key_arr` contains unique integers and `value_arr` contains strings. The function should return a dictionary where the keys are the elements from `key_arr` that are greater than 150, the values are the corresponding elements from `value_arr` converted to uppercase, and only the last occurrence of each value is stored. The keys in the dictionary should be sorted in descending order.
"""

def construct_dictionary(key_arr, value_arr):
    dictionary = {}
    for i in range(len(key_arr)):
        key = key_arr[i]
        value = value_arr[i].upper()
        if value in dictionary.values():
            continue
        if key > 150:
            dictionary[key] = value
    dictionary = dict(sorted(dictionary.items(), reverse=True))
    return dictionary