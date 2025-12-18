"""
QUESTION:
Create a function called `flatten_and_sort` that takes a single argument `array`, which is an n-dimensional array containing integers, floats, and strings. The function should return a new one-dimensional array containing all elements from the original array, sorted in ascending order. Integers and floats should be sorted numerically, and strings should be sorted lexicographically. The function should handle nested lists to any depth.
"""

def flatten_and_sort(array):
    # Flatten the array
    flat_array = []
    for sub_array in array:
        if isinstance(sub_array, list):
            flat_array.extend(flatten_and_sort(sub_array))
        else:
            flat_array.append(sub_array)

    # Split array into numbers and strings
    numbers = [x for x in flat_array if isinstance(x, (int, float))]
    strings = [x for x in flat_array if isinstance(x, str)]

    # Sort array in ascending order taking into account integers and strings
    numbers.sort()
    strings.sort()
    flat_array = numbers + strings

    return flat_array