"""
QUESTION:
Write a function `find_max_index` that takes a list of integers or floats `numbers` and an integer or float `threshold`. The function returns the index of the maximum value in `numbers` that is less than `threshold`. If no such value exists, return -1.
"""

def find_max_index(numbers, threshold):
    max_val = None
    max_index = -1

    for i in range(len(numbers)):
        if numbers[i] < threshold:
            if max_val is None or numbers[i] > max_val:
                max_val = numbers[i]
                max_index = i
    return max_index