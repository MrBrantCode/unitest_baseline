"""
QUESTION:
Create a function `find_last_index` that finds the last index of a given substring in a string. The substring should be at least two characters long and must be case-sensitive. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string. If the substring is not found in the string, the function should return -1.
"""

def find_last_index(string, substring):
    last_index = -1
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            last_index = i
    return last_index