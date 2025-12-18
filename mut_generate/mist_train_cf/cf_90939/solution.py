"""
QUESTION:
Write a function `find_occurrences` that finds all occurrences of a substring in a given string and returns the starting and ending indices of each occurrence. The function should take two parameters: `string` and `substring`. The function should return a list of tuples, where each tuple contains the starting and ending indices of an occurrence. If the substring is not found, the function should return an empty list. The function should search for overlapping occurrences.
"""

def find_occurrences(string, substring):
    occurrences = []
    start_index = 0
    while start_index < len(string):
        index = string.find(substring, start_index)
        if index == -1:
            break
        end_index = index + len(substring) - 1
        occurrences.append((index, end_index))
        start_index = index + 1
    return occurrences