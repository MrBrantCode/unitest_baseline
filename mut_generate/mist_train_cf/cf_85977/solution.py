"""
QUESTION:
Write a function `count_reverse_pairs(lst)` that takes a list of strings as input, counts the pairs of reverse strings, and returns the count. The function should ignore non-alphabet characters, be case-insensitive, and consider each pair only once.
"""

def count_reverse_pairs(lst):
    count = 0
    for i in range(len(lst)):
        str1 = ''.join(filter(str.isalpha, lst[i].lower()))
        for j in range(i+1, len(lst)):
            str2 = ''.join(filter(str.isalpha, lst[j].lower()))
            if str1 == str2[::-1]:
                count += 1
    return count