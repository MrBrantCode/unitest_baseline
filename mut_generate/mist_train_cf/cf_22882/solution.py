"""
QUESTION:
Create a function called `count_characters` that takes a string as input and returns a list of character counts, excluding special characters. The function should treat uppercase and lowercase letters as separate characters and achieve this in O(n) time complexity and O(1) space complexity relative to the input string length.
"""

def count_characters(string):
    counts = [0] * 52 # 26 for lowercase letters, 26 for uppercase letters
    for char in string:
        if 'a' <= char <= 'z':
            counts[ord(char) - ord('a')] += 1
        elif 'A' <= char <= 'Z':
            counts[ord(char) - ord('A') + 26] += 1
    return counts