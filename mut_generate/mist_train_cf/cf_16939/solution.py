"""
QUESTION:
Create a function named `repeat_string` that takes four arguments: an integer `num`, a string `string`, a boolean value `boolean`, and an array `arr`. The function should return `arr` modified to contain the `string` repeated `num` times if `boolean` is true, and also append the length of `string` to `arr` for each repetition. If `boolean` is false, return `arr` unchanged. The time complexity should not exceed O(n), where n is the number of repetitions of the string.
"""

def repeat_string(num, string, boolean, arr):
    if boolean:
        arr.extend([string] * num + [len(string)] * num)
    return arr