"""
QUESTION:
Write a function named `remove_duplicates` that takes a string as input and returns a string where consecutive duplicate characters have been removed. If the input string is empty or contains no consecutive duplicates, return the original string. The function should have a time complexity of O(n), where n is the length of the input string, and should not use any additional data structures or libraries.
"""

def remove_duplicates(string):
    if len(string) < 2:
        return string

    result = [string[0]]
    for i in range(1, len(string)):
        if string[i] != string[i-1]:
            result.append(string[i])

    return ''.join(result)