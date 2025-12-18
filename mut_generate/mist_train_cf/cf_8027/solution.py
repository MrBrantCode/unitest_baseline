"""
QUESTION:
Create a function `is_pangram_with_counts` that takes a string as input, returns `True` if the string is a pangram (contains all 26 letters of the alphabet at least once), and `False` otherwise. The function should handle both uppercase and lowercase letters, ignore non-alphabetic characters, and have a time complexity of O(n) and a space complexity of O(1).
"""

def is_pangram_with_counts(string):
    counts = [0] * 26
    string = string.lower()
    for char in string:
        if 'a' <= char <= 'z':
            counts[ord(char) - ord('a')] += 1
    return all(counts)