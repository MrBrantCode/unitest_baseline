"""
QUESTION:
Find the first non-repeating vowel character in a given string of lowercase letters, which is guaranteed to contain at least one vowel. The function should have a time complexity of O(n), where n is the length of the string, and use constant space.
"""

def firstUniqChar(s):
    vowels = 'aeiou'
    count = [0] * 5
    for char in s:
        if char in vowels:
            count[vowels.index(char)] += 1
    for char in vowels:
        if count[vowels.index(char)] == 1:
            return char