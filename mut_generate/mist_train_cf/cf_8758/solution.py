"""
QUESTION:
Implement a function called `find_target_character` that takes two parameters: a string and a target character. Using a while loop, find the index of the first occurrence of the target character in the string and return it. If the target character is not found, print "Target character not found" and return -1. The function should have a time complexity of O(n), where n is the length of the string.
"""

def find_target_character(string, target):
    index = 0
    while index < len(string):
        if string[index] == target:
            return index
        index += 1
    print("Target character not found")
    return -1