"""
QUESTION:
Design a function named `count_pattern_occurrences` that takes two parameters: `pattern` and `string`. The function should count the number of times `pattern` occurs in `string`, including overlapping occurrences. The function should be case-sensitive and should handle patterns of any length consisting of any combination of letters and numbers.
"""

def count_pattern_occurrences(pattern, string):
    count = 0
    pattern_length = len(pattern)
    string_length = len(string)

    for i in range(string_length - pattern_length + 1):
        if string[i:i+pattern_length] == pattern:
            count += 1

    return count