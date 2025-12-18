"""
QUESTION:
Write a function `count_characters` that takes a string as input and returns a list of counts for all the alphabetic characters (both lowercase and uppercase) in the string, excluding any special characters. The function should handle uppercase and lowercase letters as separate characters, have a time complexity of O(n) where n is the length of the string, and a space complexity of O(1). The function should not use any built-in functions or libraries for counting characters.
"""

def count_characters(string):
    counts = [0] * 52  # 26 for lowercase letters, 26 for uppercase letters
    for char in string:
        if 'a' <= char <= 'z':
            counts[ord(char) - ord('a')] += 1
        elif 'A' <= char <= 'Z':
            counts[ord(char) - ord('A') + 26] += 1
    return counts