"""
QUESTION:
Write a function `check_consecutive_special_characters` that takes a string as input and returns a boolean value indicating whether the string contains at least three consecutive special characters. A special character is defined as any character that is not a letter or a number. The function should be case-sensitive and count only consecutive special characters.
"""

def check_consecutive_special_characters(string):
    special_characters = set("!@#$%^&*()_-+=<>?/,.:;'{}[]|~`")
    count = 0

    for char in string:
        if char in special_characters:
            count += 1
            if count >= 3:
                return True
        else:
            count = 0

    return False