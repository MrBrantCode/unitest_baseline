"""
QUESTION:
Complete the Python function "is_happy" that takes a string "s" as input and returns True if the string is 'happy', False otherwise. A string is 'happy' if it meets the following conditions: its length is three or more, every triplet of continuous letters are unique, every distinct letter appears a minimum of twice, and no consecutive repeating letters are found. The function must use a dictionary to record the frequency of letter occurrences and avoid string manipulation methods.
"""

def is_happy(s):
    if len(s) < 3:
        return False
    letter_count = {}
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            return False
        letter_count[s[i]] = letter_count.get(s[i], 0) + 1

    letter_count[s[-1]] = letter_count.get(s[-1], 0) + 1

    for i in range(len(s)-2):
        triplet = s[i:i+3]
        if len(set(triplet)) != len(triplet) or any(letter_count[c] < 2 for c in triplet):
            return False

    return True