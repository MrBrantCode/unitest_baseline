"""
QUESTION:
Create a function `repeat_string` that takes five arguments: a number `num`, a string `string`, a boolean value `boolean`, an array `arr`, and a callback function `callback`. Return an array containing the string repeated `num` times with each string modified by the `callback` function, along with the length of each repeated string, but only if `boolean` is true. If `boolean` is false, return an empty array. The time complexity should not exceed O(n), where n is the number of repetitions of the string.
"""

def repeat_string(num, string, boolean, arr, callback):
    if boolean:
        repeated_strings = [callback(string, i) for i in range(num)]
        repeated_lengths = [len(callback(string, i)) for i in range(num)]
        return repeated_strings + repeated_lengths
    else:
        return []