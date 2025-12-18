"""
QUESTION:
Write a function `find_shortest_unique_substring` that takes a list of strings as input and returns the shortest unique substring among all strings. A unique substring is defined as a substring that does not appear in any other string in the list. If no unique substring exists, return "No unique sub-string exists." If the input list contains an empty string, return "An empty string is not considered unique." The function should have a time complexity of O(n^2) or better, where n is the total length of all strings in the input list. Both uppercase and lowercase letters should be considered unique.
"""

def find_shortest_unique_substring(strings):
    if not all(strings):  # Check if empty string is in input list
        return "An empty string is not considered unique."

    # Get all possible substrings in all strings
    substrings = [s[i: j] for s in strings for i in range(len(s)) for j in range(i + 1, len(s) + 1)]

    # Filter out substrings composed of white spaces
    substrings = [s for s in substrings if not s.isspace()]

    # Find unique substrings
    unique_substrings = [s for s in substrings if sum(s in string for string in strings) == 1]

    if unique_substrings:  # If we have any unique substrings, find the shortest one
        return min(unique_substrings, key=len)
    else:
        return "No unique sub-string exists."