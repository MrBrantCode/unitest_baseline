"""
QUESTION:
Write a function `contains_five_consecutive_special_chars` that checks if a given string contains at least five consecutive special characters. A special character is defined as any character that is not a letter or a number. The function should be case-sensitive, handle strings of any length, and return a boolean value indicating whether the string contains at least five consecutive special characters or not. The function should not use any built-in functions or libraries that directly solve the problem.
"""

def contains_five_consecutive_special_chars(string):
    count = 0  # count of consecutive special characters
    for char in string:
        if not char.isalnum():  # check if character is not a letter or a number
            count += 1
            if count >= 5:
                return True
        else:
            count = 0  # reset count if character is a letter or a number
    return False