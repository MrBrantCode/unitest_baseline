"""
QUESTION:
Create a function `countOccurrences` that takes a string and a character as input and returns the number of occurrences of the character in the string. The function should handle both lowercase and uppercase characters, consider the character at any position in the string, and handle strings with special characters and spaces. The function should not use any built-in functions or methods for counting characters, should count the occurrences in a case-sensitive manner, and should not use any additional data structures. The time complexity should be O(n), where n is the length of the input string, and the space complexity should be O(1).
"""

def countOccurrences(string, character):
    count = 0
    for c in string:
        if c == character:
            count += 1
    return count