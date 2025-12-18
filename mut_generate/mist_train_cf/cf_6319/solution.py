"""
QUESTION:
Construct a function `construct_dictionary(key_arr, value_arr)` that creates a dictionary where the keys are the elements from the `key_arr` and the values are the corresponding elements from the `value_arr`. The function should adhere to the following restrictions:
- The keys in the dictionary must be sorted in descending order.
- The values must be converted to uppercase.
- The dictionary should only include keys that are greater than 150 and have more than two digits.
- The dictionary should only include values that contain at least one vowel.
- If there are any duplicate values, the dictionary should only store the last occurrence of each value.
"""

def construct_dictionary(key_arr, value_arr):
    dictionary = {}
    for i in range(len(key_arr)):
        key = key_arr[i]
        value = value_arr[i].upper()
        if key > 150 and len(str(key)) > 2:
            if any(char in value for char in "AEIOUaeiou"):
                dictionary[key] = value

    sorted_keys = sorted(dictionary.keys(), reverse=True)
    sorted_dictionary = {}
    for key in sorted_keys:
        sorted_dictionary[key] = dictionary[key]

    final_dictionary = {}
    unique_values = []
    for key, value in sorted_dictionary.items():
        if value not in unique_values:
            final_dictionary[key] = value
            unique_values.append(value)

    return final_dictionary