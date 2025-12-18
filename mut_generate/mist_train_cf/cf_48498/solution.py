"""
QUESTION:
Write a function named `exchange` that takes two lists of integers as input, `lst1` and `lst2`, and returns "YES" if it's possible to exchange elements between the lists to transform `lst1` into a list of only even numbers while maintaining the overall sum of both lists, and "NO" otherwise. The input lists will always contain at least one integer.
"""

def exchange(lst1, lst2):
    s1, s2 = sum(lst1), sum(lst2)
    for i in lst1:
        for j in lst2:
            new_s1, new_s2 = s1 - i + j, s2 - j + i
            if new_s1 % 2 == 0 and new_s2 % 2 == 0:
                return 'YES'
    return 'NO'