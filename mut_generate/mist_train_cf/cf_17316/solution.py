"""
QUESTION:
Write a function `minimum_edit_distance(str1, str2)` that calculates the minimum string edit distance between two strings of different lengths. The allowed operations are insertion, deletion, and substitution of a single character. The function should have a time complexity of O(m*n) and space complexity of O(min(m, n)), where m and n are the lengths of str1 and str2 respectively.
"""

def minimum_edit_distance(str1, str2):
    m, n = len(str1), len(str2)
    if m == 0:
        return n
    if n == 0:
        return m
    if m > n:
        str1, str2 = str2, str1
        m, n = n, m
    previous_row = range(n + 1)
    for i, char1 in enumerate(str1, 1):
        current_row = [i]
        for j, char2 in enumerate(str2, 1):
            insertions = previous_row[j] + 1
            deletions = current_row[j - 1] + 1
            substitutions = previous_row[j - 1] + (char1 != char2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[n]