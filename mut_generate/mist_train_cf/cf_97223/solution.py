"""
QUESTION:
Write a function called `find_substring` that takes two arguments, `string` and `substring`, and returns a list of all starting indices where `substring` appears in `string`. The function should return all indices, including overlapping matches. If `substring` is not found, the function should return an empty list.
"""

def find_substring(string, substring):
    indices = []
    index = -1
    while True:
        index = string.find(substring, index + 1)
        if index == -1:
            break
        indices.append(index)
    return indices