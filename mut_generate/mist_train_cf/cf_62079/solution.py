"""
QUESTION:
Write a function named count_reverse_pairs that takes a list of strings as input. The function should count the pairs of strings that are reverse of each other, ignoring non-alphabetical characters (special characters and numbers). The function should return the total count of such pairs.
"""

def count_reverse_pairs(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            str1 = ''.join(e for e in lst[i] if e.isalpha())
            str2 = ''.join(e for e in lst[j] if e.isalpha())
            if str1 == str2[::-1]:
                count += 1
    return count