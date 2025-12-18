"""
QUESTION:
Write a function called `is_happy` that determines whether a given string is 'happy'. A string is 'happy' if its length is at least 3, every triplet of subsequent letters has unique characters, every unique letter appears at least twice, and no letter appears consecutively. Use a dictionary to count the frequency of characters in the string.
"""

def is_happy(s):
    if len(s) < 3:
        return False
    counter_dict = {}
    for i in range(len(s)-2):
        substring = s[i:i+3]
        if len(set(substring)) != 3:
            return False
        for char in substring:
            if char not in counter_dict:
                counter_dict[char] = 1
            else:
                counter_dict[char] += 1
            if substring.count(char) > 1:
                return False
    for count in counter_dict.values():
        if count < 2:
            return False
    return True