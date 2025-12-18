"""
QUESTION:
Implement a function `is_anagram(s1, s2)` that takes two strings `s1` and `s2` as input and returns a tuple containing a boolean indicating whether the strings are anagrams of each other and the number of steps taken to make the determination. The function should only consider lowercase alphabets and should not use built-in library functions or data structures.
"""

def is_anagram(s1, s2):
    steps = 0
    if len(s1) != len(s2):
        return False, steps
    lst_s1 = [0] * 26
    lst_s2 = [0] * 26

    for i in range(len(s1)):
        steps += 1
        lst_s1[ord(s1[i]) - ord('a')] += 1
        lst_s2[ord(s2[i]) - ord('a')] += 1

    for i in range(26):
        steps += 1
        if lst_s1[i] != lst_s2[i]:
            return False, steps

    return True, steps