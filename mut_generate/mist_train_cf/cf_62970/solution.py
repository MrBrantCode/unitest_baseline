"""
QUESTION:
Write a function `check_appellation(name)` that checks if a given appellation consists of exactly five alphabetical characters. The function should return `True` only when the appellation is precisely 5 characters long and all of them are alphabetic. Consider edge cases such as white spaces, special characters, and numbers. The function should be case insensitive, meaning it should consider both lowercase and uppercase letters as valid inputs. Also, ensure the input is not `None` and is an instance of `str`.
"""

def check_appellation(name):
    if not name or not isinstance(name, str):
        return False
    name = name.lower() # convert to lowercase
    if len(name) != 5:
        return False
    for ch in name:
        if not ch.isalpha(): 
            return False
    return True