"""
QUESTION:
Create a function named `find_substring` that takes two parameters: `string` and `substring`. The function should return a boolean indicating whether `substring` is present in `string` and an integer representing the index at which `substring` is found in `string`. If `substring` is not found in `string`, the function should return `False` and `-1` as the index.
"""

def find_substring(string, substring):
    # Find the index of the substring in the string
    index = string.find(substring)

    # If the substring is found, return True and the index
    if index != -1:
        return True, index

    # If the substring is not found, return False and -1 as the index
    return False, -1