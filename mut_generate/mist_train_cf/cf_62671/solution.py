"""
QUESTION:
Write a function `is_decimal_between_0_and_1000(s)` that checks if a given string `s` is a decimal number with a precision of 2, is positive, and falls within the range 0 to 1000. The function should return True if all conditions are met, False otherwise.
"""

def is_decimal_between_0_and_1000(s):
    try:
        number = float(s)

        if number <= 0 or number >= 1000:
            return False
            
        if s.count('.') == 1:
            # if precision is less than 2 return False
            if len(s[s.index('.'):]) < 3:
                return False
            
        elif s.count('.') > 1:
            return False
            
        if not s.replace('.', '', 1).isdigit():
            return False
            
        return True
    except ValueError:
        return False