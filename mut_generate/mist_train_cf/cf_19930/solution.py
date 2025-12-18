"""
QUESTION:
Find the length of the longest string between two substrings. The function `find_longest_string` should take three parameters: a string, a start substring, and an end substring. The function should be case-insensitive and return the length of the string between the start and end substrings. If the start or end substrings are not found in the string, the function should return 0.
"""

def find_longest_string(s, start, end):
    s = s.lower()
    start = start.lower()
    end = end.lower()

    start_index = s.find(start)
    if start_index == -1:
        return 0

    end_index = s.find(end, start_index + len(start))
    if end_index == -1:
        return 0

    return end_index - start_index