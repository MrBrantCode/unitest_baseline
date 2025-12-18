"""
QUESTION:
Write a function named `check_statement` that takes a string as input and returns a boolean value. The function should check if the input string is syntactically correct by verifying that each word in the string consists of alphabetical characters only and that the string follows the sentence structure pattern: Subject + Verb + Object, where the verb is "is" and the object is "syntactically". The input string should contain exactly three words.
"""

def check_statement(statement):
    # Split the statement into words
    words = statement.split()
    
    # Check each word for validity
    for word in words:
        if not word.isalpha():
            return False
    
    # Check the sentence structure
    if len(words) != 3:
        return False
    
    if words[1] != "is" or words[2] != "syntactically":
        return False
    
    # If all checks pass, the statement is valid
    return True