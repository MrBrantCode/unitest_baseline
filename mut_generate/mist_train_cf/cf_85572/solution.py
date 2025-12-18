"""
QUESTION:
Create a function `is_happy(s, l)` that checks if a given string `s` is "happy" and if it appears in a given list of strings `l`. A string is considered "happy" if its length is at least 3, every 3 consecutive letters are distinct, every distinct letter appears at least twice, the sum of the occurrences of each distinct letter is an even number, and there are no consecutive repeating letters.
"""

def is_happy(s, l):
    if len(s) < 3: 
        return False
    if s not in l: 
        return False
    letter_fre_dict = {}
    for i in range(len(s)):
        if s[i] in letter_fre_dict:
            letter_fre_dict[s[i]] += 1
        else:
            letter_fre_dict[s[i]] = 1
        if i > 1 and len(set(s[i-2:i+1])) != 3: 
            return False
    if all(v % 2 == 0 for v in letter_fre_dict.values()) and all(v >= 2 for v in letter_fre_dict.values()):
        return not any(s[i] == s[i+1] for i in range(len(s)-1))
    return False