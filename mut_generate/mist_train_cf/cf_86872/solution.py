"""
QUESTION:
Write a function `has_consecutive_uv` that takes a string as input and returns a boolean value. The function should return `True` if the string contains consecutive "u" and "v" characters, ignoring any occurrences of "uv" and "vu". The function should return `False` otherwise.
"""

def has_consecutive_uv(string):
    ignore_uv = False
    ignore_vu = False
    
    for i in range(len(string) - 1):
        if ignore_uv or ignore_vu:
            ignore_uv = False
            ignore_vu = False
            continue
        
        if string[i] == "u" and string[i+1] == "v":
            ignore_uv = True
        elif string[i] == "v" and string[i+1] == "u":
            ignore_vu = True
        elif string[i] == "u" and string[i+1] == "u":
            return True
        elif string[i] == "v" and string[i+1] == "v":
            return True
    
    return False