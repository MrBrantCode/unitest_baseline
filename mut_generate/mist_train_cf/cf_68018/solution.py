"""
QUESTION:
Develop a function named `split_and_mirror` that takes an array of distinct integer values as input. The function should split the array into two equal-length sections and check if they are mirrored. If the array length is not even, return an error message. If the sections are not mirrored, return an error message. Otherwise, return the two mirrored sections. The function should be able to handle arrays with an even number of elements.
"""

def split_and_mirror(arr):
    # Check array length
    if len(arr) % 2 != 0:
        return "Array length is not even, cannot be split into two equal sections."

    middle_index = len(arr) // 2

    # Split array into two parts
    left_part = arr[:middle_index]
    right_part = arr[middle_index:]

    # Mirror the right part and check if both parts are equal
    if left_part == right_part[::-1]:
        return (left_part, right_part[::-1])
    else:
        return "Array cannot be split into mirrored parts."