"""
QUESTION:
Write a function named `correct_bracketing` that takes a string `brackets` consisting of "<" and ">" characters and returns a boolean value indicating whether each opening bracket "<" has a matching closing bracket ">".
"""

def correct_bracketing(brackets):
    """
    This function checks if each opening bracket "<" has a matching closing bracket ">" in a given string.
    
    Args:
        brackets (str): A string consisting of "<" and ">" characters.
    
    Returns:
        bool: True if each opening bracket has a matching closing bracket, False otherwise.
    """
    count = 0
    for bracket in brackets:
        if bracket == "<":
            count += 1
        elif bracket == ">":
            count -= 1
            if count < 0:
                return False
    return count == 0