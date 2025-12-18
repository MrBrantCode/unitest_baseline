"""
QUESTION:
Write a function `validate_ip(s)` that checks if a given string `s` is a valid IP address, either IPV4 or IPV6, and returns `True` if valid and `False` otherwise. The function should adhere to the following rules:
- IPV4: 4 parts separated by ".", each part is a number from 0 to 255, and cannot start with 0 unless it is 0 itself.
- IPV6: 8 parts separated by ":", each part is a 4-digit hexadecimal number and can start with 0.
- The IP address should not contain any leading or trailing spaces.
"""

def validate_ip(s):
    if "." in s: # checking for IPV4
        p = s.split('.')
        if len(p) != 4: # An IPV4 must have 4 parts
            return False
        for pp in p:
            if len(pp) > 3 or len(pp) == 0 or not pp.isdigit():
                return False
            if int(pp) < 0 or int(pp) > 255:
                return False
            if len(pp) > 1 and pp[0] == '0':
                return False
        return True
    elif ":" in s: # checking for IPV6
        p = s.split(':')
        if len(p) != 8: # An IPV6 must have 8 parts
            return False
        for pp in p:
            if len(pp) > 4 or len(pp) <= 0:
                return False
            for letter in pp:
                if not (letter.isdigit() or 'a' <= letter <= 'f' or 'A' <= letter <= 'F'):
                    return False
        return True
    return False