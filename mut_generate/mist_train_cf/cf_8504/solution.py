"""
QUESTION:
Write a function `find_consonants(string)` that takes a string as input and returns the starting index of the substring that contains all the consonants 'bcdfghjklmnpqrstvwxyz' in the same order as they appear in the English alphabet. The consonants must appear consecutively in the substring. If no such substring exists, return -1.
"""

def find_consonants(string):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    i = 0
    while i <= len(string) - len(consonants):
        if string[i:i+len(consonants)] == consonants:
            return i
        i += 1
    return -1