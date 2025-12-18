"""
QUESTION:
Write a function called `find_occurrences` that finds all occurrences of a given substring in a string and returns a list of tuples containing the starting and ending indices of each occurrence. The function should take two parameters: `string` and `substring`, and it should return a list of tuples where each tuple contains two integers representing the starting and ending indices of an occurrence.
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