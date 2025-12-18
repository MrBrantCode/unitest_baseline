"""
QUESTION:
Implement the function `modify_sequence_and_identify_uniqueness(s, t)` that takes two strings `s` and `t` as input. Replace every character in `s` that is present in `t` with '*'. Then, check if there are any recurrent characters in the resulting string. If no recurrent characters are present, return the modified string along with "Unique". If recurrent characters exist, return the modified string along with "Non-unique".
"""

def modify_sequence_and_identify_uniqueness(s, t):
    t_set = set(t)
    s_set = set()

    modified_s = ''.join('*' if c in t_set else c for c in s)

    for c in modified_s:
        if c != '*':
            s_set.add(c)

    status = "Unique" if len([c for c in modified_s if c != '*']) == len(s_set) else "Non-unique"

    return modified_s, status