"""
QUESTION:
Create a function named `check_anagram` that takes two strings `s1` and `s2` containing only lower case alphabets. The function should check if `s2` is an anagram of any substring of `s1` and return the index of the beginning of the substring in `s1` if it exists, otherwise return -1.
"""

def check_anagram(s1, s2):
    s2_len = len(s2)
    s2_sorted = ''.join(sorted(s2))

    for i in range(len(s1) - s2_len + 1):
        s1_sub = s1[i:i+s2_len]
        if ''.join(sorted(s1_sub)) == s2_sorted:
            return i
  
    return -1  # Return -1 to indicate no anagram substring was found