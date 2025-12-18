"""
QUESTION:
Create a function `countOccurrences` that takes two parameters: a string and a character. The function should count the occurrences of the given character in the string, handling both lowercase and uppercase characters, and return the count. The function must have a constant space complexity of O(1), not use any built-in functions or methods for counting characters, and achieve a time complexity of O(n), where n is the length of the input string.
"""

def countOccurrences(string, character):
    count = 0
    for c in string:
        if c.lower() == character.lower():
            count += 1
    return count