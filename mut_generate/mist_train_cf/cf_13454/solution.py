"""
QUESTION:
Create a function `check_strings` that takes two strings `s1` and `s2` as input, and returns `True` if `s1` can be transformed into `s2` by replacing sequences of identical characters in `s1` with a single character followed by an asterisk and the count of consecutive occurrences, and `False` otherwise.
"""

def check_strings(s1, s2):
    pointer_s1 = 0
    pointer_s2 = 0
    
    while pointer_s1 < len(s1) and pointer_s2 < len(s2):
        if s1[pointer_s1] == s2[pointer_s2]:
            pointer_s1 += 1
            pointer_s2 += 1
        elif s2[pointer_s2] == '*':
            pointer_s2 += 1
        elif s2[pointer_s2].isdigit():
            count = int(s2[pointer_s2])
            pointer_s2 += 1
            if s1[pointer_s1:pointer_s1+count] == s1[pointer_s1] * count:
                pointer_s1 += count
            else:
                return False
        else:
            return False
    
    if pointer_s1 == len(s1) and pointer_s2 == len(s2):
        return True
    else:
        return False