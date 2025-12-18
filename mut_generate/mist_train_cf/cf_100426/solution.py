"""
QUESTION:
Write a function find_string_with_all_vowels that takes a list of strings as input and returns the index and the first string that contains all the vowels (a, e, i, o, u) in order. If no such string exists, return -1 and print a warning message. The time complexity should be O(n).
"""

def find_string_with_all_vowels(lst):
    vowels = 'aeiou'
    for i, s in enumerate(lst):
        j = 0
        for c in s:
            if j == 5:
                return i, s
            if c == vowels[j]:
                j += 1
        if j == 5:
            return i, s
    print('No string found with all vowels.')
    return -1, None