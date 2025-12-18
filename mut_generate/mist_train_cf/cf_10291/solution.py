"""
QUESTION:
Create a function named `repeat_string` that takes three arguments: an integer `num`, a string `string`, and a boolean `boolean`. The function should return `string` repeated `num` times if `boolean` is `True`; otherwise, it should return an empty string. The function must achieve this in linear time complexity, O(n), where n is the number of repetitions of the string.
"""

def repeat_string(num, string, boolean):
    if boolean:
        return string * num
    else:
        return ""