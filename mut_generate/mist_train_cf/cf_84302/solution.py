"""
QUESTION:
Write a function called `solve` that takes a list of strings (`list_of_strings`) and a substring as input. The function should return a list containing tuples, where each tuple includes a string from `list_of_strings` that has the given substring and the count of occurrences of the substring in that string. The returned list should only include strings with at least one occurrence of the substring.
"""

def solve(list_of_strings, substring):
    result = []
    for string in list_of_strings:
        count = string.count(substring)
        if count > 0:
            result.append((string, count))
    return result