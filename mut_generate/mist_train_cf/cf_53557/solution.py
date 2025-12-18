"""
QUESTION:
Write a function `is_happy(s)` that takes a string `s` as input and checks if it's happy. A string is happy if it meets the following conditions:
- It contains only lowercase letters and no special characters.
- Its length is at least 3.
- Every 3 consecutive letters are distinct.
- Every distinct letter appears at least twice.
- There are no consecutive repeating letters.
- The sum of the occurrences of each distinct letter is an even number.
- No more than two distinct letters can have the same occurrences.

You must use a dictionary and a set to solve this problem.
"""

def is_happy(s):
    import re

    if not re.match("^[a-z]+$", s):
        return False
    
    if len(s) < 3:
        return False

    letter_dict = {}
    letter_set = set()

    for i in range(len(s)):
        if s[i] in letter_dict:
            letter_dict[s[i]] += 1
        else:
            letter_dict[s[i]] = 1
        letter_set.add(s[i])
        if i < len(s) - 2 and s[i] == s[i+1] == s[i+2]:
            return False
        if i < len(s) - 1 and s[i] == s[i + 1]:
            return False

    if len(letter_set) < 3:
        return False

    count_dict = {}
    for count in letter_dict.values():
        if count in count_dict:
            count_dict[count] += 1
        else:
            count_dict[count] = 1
        if count % 2 != 0:
            return False

    if max(count_dict.values()) > 2:
        return False

    return True