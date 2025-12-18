"""
QUESTION:
Create a function `is_anagram(s1, s2)` that checks if two input strings are anagrams of each other. The function should be case insensitive and handle unicode strings. It should return a boolean value indicating whether the strings are anagrams. The function should have a time complexity of O(n), where n is the length of the input strings.
"""

def entrance(s1, s2):
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()
    if len(s1) != len(s2):
        return False
    count = {}
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            return False
    for k in count:
        if count[k]!=0:
            return False
    return True