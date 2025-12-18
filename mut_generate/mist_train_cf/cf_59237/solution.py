"""
QUESTION:
Create a function `process_strings` that takes a list of strings as input. The function should return a new list containing the reversed and capitalized versions of the input strings that consist only of letters, sorted in descending lexicographical order. The function should exclude strings that contain special characters or numbers.
"""

def process_strings(lst):
    result = []
    for s in lst:
        if s.isalpha():
            result.append(s.upper()[::-1])
    result.sort(reverse=True)
    return result