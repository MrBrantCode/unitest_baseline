"""
QUESTION:
Write a function `find_consonants` that takes a string as input and returns the starting index of the substring that contains all the consonants in the English alphabet in the same order as they appear in the alphabet. The consonants must appear consecutively. If no such substring exists, return -1. The function should be case-sensitive and consider only lowercase letters.
"""

def find_consonants(string):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    i = 0
    while i <= len(string) - len(consonants):
        if string[i:i+len(consonants)] == consonants:
            return i
        i += 1
    return -1