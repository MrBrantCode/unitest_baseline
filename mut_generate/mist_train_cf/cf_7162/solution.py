"""
QUESTION:
Construct a function `find_last_index` that takes two parameters: `string` and `substring`. The function should return the last index of the given `substring` in the `string` in a case-sensitive manner, assuming the `substring` is at least two characters long and the `input string` contains at least one occurrence of the `substring`. If the `substring` is not found in the `string`, the function should return -1. The function should achieve a time complexity of O(n), where n is the length of the `input string`, and a space complexity of O(1).
"""

def find_last_index(string, substring):
    last_index = -1
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            last_index = i
    return last_index