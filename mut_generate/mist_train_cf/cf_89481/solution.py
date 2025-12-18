"""
QUESTION:
Write a function `count_characters` that takes a string `s` as input and returns a dictionary where the keys are the unique characters in the string and the values are the counts of each character. The input string consists only of lowercase letters, numbers, and special characters. The function should have a time complexity of O(n) and a space complexity of O(k), where n is the length of the input string and k is the number of unique characters in the string.
"""

def count_characters(s):
    char_count = {}
    
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count