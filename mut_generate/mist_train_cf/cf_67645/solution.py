"""
QUESTION:
Create a function `find_repeating_substring` that determines if a given string `s` ends with a specified substring `sub` and also repeats after specific intervals throughout the entire string `s`. The function should return `True` if the substring repeats at uniform gaps throughout the string and ends with the string, and `False` otherwise.
"""

def find_repeating_substring(s, sub):
    sub_len = len(sub)
    if s.endswith(sub):  
        indices = [i for i in range(len(s)) if s.startswith(sub, i)]
        if len(indices) < 2:
            return False
        diff = indices[1] - indices[0]
        for i in range(1, len(indices)-1):
            if indices[i+1] - indices[i] != diff:
                return False
        return True
    return False