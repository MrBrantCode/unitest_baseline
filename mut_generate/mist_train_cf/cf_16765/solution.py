"""
QUESTION:
Write a function `count_substring(string, substring)` that counts the number of occurrences of a specific substring in a given string, ignoring any occurrences of the substring within another substring. The function should be case-sensitive. The input string and substring are not empty, and the substring is not longer than the string.
"""

def count_substring(string, substring):
    count = 0
    index = 0
    while index < len(string):
        if string[index:index+len(substring)] == substring:
            count += 1
            index += len(substring)
        else:
            index += 1
    return count