"""
QUESTION:
Write a function named `find_longest_string` that takes a list of strings as input and returns the longest string that only contains alphabetic characters, excluding any strings that contain numbers or special characters. The function should have a time complexity of O(n), where n is the total number of characters in all the strings combined, and should not use any built-in functions or libraries that directly solve this problem.
"""

def find_longest_string(strings):
    longest_string = ""
    for string in strings:
        if not any(char.isdigit() or not char.isalpha() for char in string):
            if len(string) > len(longest_string):
                longest_string = string
    return longest_string