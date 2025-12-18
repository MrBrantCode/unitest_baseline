"""
QUESTION:
Write a function `count_reverse_pairs` that takes a list of strings as input and returns the number of pairs of strings that are reverses of each other. The function should be case-insensitive and ignore non-alphanumeric characters and spaces when comparing strings.
"""

def count_reverse_pairs(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            str_i = ''.join(e for e in lst[i] if e.isalnum()).lower().replace(' ', '')
            str_j = ''.join(e for e in lst[j] if e.isalnum()).lower().replace(' ', '')
            if str_i == str_j[::-1]:
                count += 1
    return count