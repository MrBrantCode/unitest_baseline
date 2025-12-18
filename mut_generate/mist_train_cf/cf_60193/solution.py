"""
QUESTION:
Create a function `analyze_string_complex(s)` that scrutinizes an input string `s`. If `s` contains a comma or a colon, return a list of words separated by the delimiter and a list of indices where the delimiter is found. If `s` does not contain a comma or a colon, return the count and indices of lowercase alphabetic characters with odd ord() values (using an ordinal baseline where 'a' is 0, 'b' is 1, through to 'z' being 25).
"""

def analyze_string_complex(s):
    if ',' in s:
        return s.split(','), [i for i, char in enumerate(s) if char == ',']
    elif ':' in s:
        return s.split(':'), [i for i, char in enumerate(s) if char == ':']
    else:
        lowercase_odd_ord_chars = [char for char in s if char.islower() and (ord(char) - ord('a')) % 2 == 1]
        return len(lowercase_odd_ord_chars), [i for i, char in enumerate(s) if char in lowercase_odd_ord_chars]