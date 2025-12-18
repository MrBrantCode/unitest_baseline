"""
QUESTION:
Implement the function `find_pattern(string, pattern)` that finds the first index of the pattern in the string. The pattern can contain the following wildcards: '*' to match any sequence of characters, '?' to match any single character, and '+' to match any single digit character. The input string will not contain any non-alphanumeric characters (except for whitespaces). If the pattern is not found, return -1.
"""

def find_pattern(string, pattern):
    str_len = len(string)
    pat_len = len(pattern)
    
    def match(i, j):
        if j == pat_len:
            return True
        if i >= str_len:
            return False
        if pattern[j] == '*':
            return match(i, j+1) or (i < str_len and match(i+1, j))
        elif pattern[j] == '?':
            return match(i+1, j+1)
        elif pattern[j] == '+':
            return i < str_len and string[i].isdigit() and match(i+1, j+1)
        else:
            return i < str_len and string[i] == pattern[j] and match(i+1, j+1)

    for i in range(str_len - pat_len + 1):
        if match(i, 0):
            return i
    
    return -1