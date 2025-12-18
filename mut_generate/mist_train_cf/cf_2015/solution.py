"""
QUESTION:
Create a function named `repeat_string` that takes in five parameters: an integer `num`, a string `string`, a boolean `boolean`, a list `arr`, and a callback function `callback`. The function should return a list containing the modified string repeated `num` times using the provided callback function if `boolean` is True. The list should also include the length of each repeated string. If `boolean` is False, return an empty list. The time complexity should not exceed O(n), where n is the number of repetitions of the string.
"""

def repeat_string(num, string, boolean, arr, callback):
    if boolean:
        return [callback(string, i) for i in range(num)] + [len(callback(string, i)) for i in range(num)]
    else:
        return []