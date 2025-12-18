"""
QUESTION:
Write a function named `count_characters` that takes a string as input and returns the count of each alphabetic character (both uppercase and lowercase) in the string, excluding any special characters. The function should not use any built-in functions or libraries for counting characters. The function should treat uppercase and lowercase letters as separate characters.
"""

def count_characters(string):
    character_count = {}

    for char in string:
        if ord(char) in range(97, 123) or ord(char) in range(65, 91):
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1

    return character_count