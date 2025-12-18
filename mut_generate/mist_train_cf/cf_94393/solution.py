"""
QUESTION:
Write a function named `count_substring` that takes two parameters, `string` and `substring`, and returns the number of times the `substring` appears in the `string` without counting occurrences within another `substring`. The function must be case-sensitive.
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