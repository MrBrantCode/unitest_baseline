"""
QUESTION:
Write a function `isValidString(s)` that takes a string `s` composed only of lowercase English alphabets without any special characters, and returns `True` if the string is valid, and `False` otherwise. A valid string must meet the following conditions:
- It has a minimum length of 6.
- Every six consecutive characters are distinct.
- All unique characters occur an even number of times.
- The maximum count for unique characters with the same frequency is not more than 3.
"""

from collections import Counter

def isValidString(s):
    # Checking if input string meets criteria 1
    if len(s) < 6:
        return False

    # Checking if input string meets criteria 2 and 3
    cnt = Counter(s)
    for i in range(len(s)-5):
        if len(set(s[i:i+6])) != 6:
            return False
        for key in cnt.keys():
            if cnt[key] % 2 != 0:
                return False

    # Checking if input string meets criteria 4
    frequency_counter = Counter(cnt.values())
    for value in frequency_counter.values():
        if value > 3:
            return False

    return True