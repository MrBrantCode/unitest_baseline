"""
QUESTION:
Write a function `check_statement(statement)` that takes a string `statement` as input and returns a boolean value indicating whether the statement is syntactically correct and follows a specific sentence structure pattern. The rules for word validity and sentence structure are as follows:

- A word is considered valid if it consists of alphabetical characters only.
- The sentence structure should follow the pattern: Subject + Verb + Object, where the verb is "is" and the object is "syntactically".
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