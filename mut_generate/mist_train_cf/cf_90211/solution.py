"""
QUESTION:
Write a function `is_pangram_with_counts` that takes a string as input and returns a boolean value indicating whether the string is a pangram, along with the counts of all letters. The function should have a time complexity of O(n) and a space complexity of O(1), handle both uppercase and lowercase letters, and count non-alphabetic characters.
"""

def is_pangram_with_counts(string):
    counts = [0] * 26
    string = string.lower()
    for char in string:
        if 'a' <= char <= 'z':
            counts[ord(char) - ord('a')] += 1
    return all(counts)