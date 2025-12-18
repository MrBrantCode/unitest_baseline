"""
QUESTION:
Write a function named "removeDuplicates" that takes a string "s" as input and returns a string with all duplicate characters removed, keeping only the first occurrence of each character. The function should have a time complexity of O(n), where n is the length of the input string, and use a single integer variable as an additional data structure to keep track of the characters encountered. The input string may contain any ASCII characters and can have a maximum length of 10^6 characters.
"""

def removeDuplicates(s):
    result = ''
    encountered = 0
    for char in s:
        ascii_value = ord(char)
        if not (encountered & (1 << ascii_value)):
            result += char
            encountered |= 1 << ascii_value
    return result