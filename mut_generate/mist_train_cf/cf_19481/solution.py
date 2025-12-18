"""
QUESTION:
Write a function called `count_a` that takes a string as input and returns the number of times the characters 'a' and 'á' (case-insensitive) appear in the string. The function should handle strings of any length, including Unicode characters, and have a time complexity of O(n), where n is the length of the string. Implement the logic to iterate through the string and count the occurrences without using built-in string manipulation functions or regular expressions.
"""

def count_a(s):
    count = 0
    for char in s:
        if char.lower() == 'a' or char.lower() == 'á':
            count += 1
    return count