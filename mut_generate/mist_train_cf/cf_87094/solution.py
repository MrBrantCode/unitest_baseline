"""
QUESTION:
Write a function named `contains_five_consecutive_special_chars` that checks if a given string contains at least five consecutive special characters, where special characters are defined as any character that is not a letter or a number. The function should be case-sensitive and handle strings of any length, returning a boolean value indicating whether the string contains at least five consecutive special characters or not. Do not use any built-in functions or libraries that directly solve the problem.
"""

def contains_five_consecutive_special_chars(string):
    count = 0  
    for char in string:
        if not char.isalnum():  
            count += 1
            if count >= 5:
                return True
        else:
            count = 0  
    return False