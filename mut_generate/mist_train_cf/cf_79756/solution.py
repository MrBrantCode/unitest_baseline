"""
QUESTION:
Write a function named count_reverse_pairs that takes a list of strings as input. The function should return the number of pairs of reverse strings in the list. The function should be case-insensitive and should ignore spaces, special characters, and numbers while counting the pairs of reverse strings.
"""

def count_reverse_pairs(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            clean_i = ''.join(e for e in lst[i] if e.isalpha()).lower().replace(' ', '')
            clean_j = ''.join(e for e in lst[j] if e.isalpha()).lower().replace(' ', '')
            if clean_i == clean_j[::-1]:
                count += 1
    return count