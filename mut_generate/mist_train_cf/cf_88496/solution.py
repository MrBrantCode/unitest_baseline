"""
QUESTION:
Implement a function `find_longest_string(strings)` that takes a list of strings as a parameter, where the longest string is determined by the sum of the ASCII values of its characters. If there are multiple strings with the same maximum sum, print all of them in the order they appear in the original list. The function should raise a custom exception `EmptyListException` if the list is empty or contains only empty strings.
"""

class EmptyListException(Exception):
    pass

def find_longest_string(strings):
    if not strings:
        raise EmptyListException("List is empty.")
    
    longest_strings = []
    max_sum = float('-inf')
    
    for string in strings:
        string_sum = sum(ord(char) for char in string)
        if string_sum > max_sum:
            longest_strings = [string]
            max_sum = string_sum
        elif string_sum == max_sum:
            longest_strings.append(string)
    
    if not longest_strings:
        raise EmptyListException("List contains only empty strings.")
    
    return longest_strings