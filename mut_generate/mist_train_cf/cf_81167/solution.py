"""
QUESTION:
### Move Zeros to End of Array

Create a Python method `move_zeros(array)` that takes a nested array of varying depth and length as input, and moves all occurrences of the integer zero to the end of the array while maintaining the sequential order of non-zero elements. The method should be able to handle arrays comprising multiple data types, including integers, strings, floats, dictionaries, sets, and tuples, and should exclusively move the integer zero to the end of the array. The method should also be able to handle circular arrays, empty arrays, and arrays with a large number of elements (up to 10^6) efficiently. 

The method should be implemented without using any pre-existing Python functions or libraries to directly resolve the issue.
"""

def move_zeros(array):
    if isinstance(array, dict):
        for key in array:
            array[key] = move_zeros(array[key])
    elif isinstance(array, set):
        new_set = set()
        count_zero = 0
        for item in array:
            if item == 0:
                count_zero += 1
            else:
                new_set.add(move_zeros(item))
        for i in range(count_zero):
            new_set.add(0)
        return new_set
    elif isinstance(array, list):
        new_array = []
        count_zero = 0
        for item in array:
            if item == 0:
                count_zero += 1
            else:
                new_array.append(move_zeros(item))
        for i in range(count_zero):
            new_array.append(0)
        return new_array
    elif isinstance(array, tuple):
        new_array = []
        count_zero = 0
        for item in array:
            if item == 0:
                count_zero += 1
            else:
                new_array.append(move_zeros(item))
        for i in range(count_zero):
            new_array.append(0)
        return tuple(new_array)
    else:
        return array