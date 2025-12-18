"""
QUESTION:
Create a function `repeat_string` that takes four arguments: `num` (a number), `string`, `boolean` (a boolean value), and `arr` (an array). If `boolean` is `True`, return `arr` extended with `string` repeated `num` times and the length of `string` repeated `num` times; otherwise, return an empty array. The time complexity should not exceed O(n), where n is the number of repetitions of the string.
"""

def repeat_string(num, string, boolean, arr):
    if boolean:
        arr.extend([string] * num + [len(string)] * num)
    return arr