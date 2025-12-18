"""
QUESTION:
Write a function called `find_longest_string` that takes two parameters: a list of strings and an integer `k`. It should return the longest string from the list with a length of `k` or less. If multiple strings have the same maximum length, return the lexicographically smallest one.
"""

def find_longest_string(strings, k):
    longest_string = ""
    for string in strings:
        if len(string) <= k and (len(string) > len(longest_string) or (len(string) == len(longest_string) and string < longest_string)):
            longest_string = string
    return longest_string