"""
QUESTION:
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.
"""

def is_valid_number(s: str) -> bool:
    dot = False
    exp = False
    
    try:
        # Trim leading and trailing spaces
        while s.startswith(' '):
            s = s[1:]
        while s.endswith(' '):
            s = s[:-1]
        
        # Handle leading sign
        if s.startswith('-') or s.startswith('+'):
            s = s[1:]
    except IndexError:
        return False
    
    # Check for empty string after trimming
    if s == '':
        return False
    
    # Check for invalid starting character
    if s.startswith('e'):
        return False
    
    # Check for invalid ending character
    if (s[-1] > '9' or s[-1] < '0') and s[-1] != '.':
        return False
    
    # Handle starting dot
    if s.startswith('.'):
        if len(s) == 1:
            return False
        elif s[1] < '0' or s[1] > '9':
            return False
    
    i = 0
    while i < len(s):
        if s[i] < '0' or s[i] > '9':
            if s[i] == '.':
                if not dot and (not exp):
                    dot = True
                else:
                    return False
            elif s[i] == 'e':
                if not exp:
                    exp = True
                    if s[i + 1] == '-' or s[i + 1] == '+':
                        i = i + 1
                else:
                    return False
            else:
                return False
        i = i + 1
    
    return True