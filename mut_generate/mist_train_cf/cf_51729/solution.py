"""
QUESTION:
Implement the `myAtoi` function, which converts a string to a 32-bit signed integer with additional operations. The function should read in and ignore any leading whitespace, handle '+' and '-' signs, and convert digits into an integer. If the string contains a decimal point ('.'), consider the number after the decimal point as a fraction and convert it to a decimal number. If the string contains a percentage sign ('%'), consider the number before the percentage sign as a percentage and convert it to a decimal number. The function should clamp the integer if it's out of the 32-bit signed integer range `[-231, 231 - 1]`. 

Constraints: `0 <= s.length <= 200`, and `s` consists of English letters (lower-case and upper-case), digits (`0-9`), `' '`, `'+'`, `'-'`, `'.'`, and `'%'`.
"""

INT_MAX = 2**31 - 1
INT_MIN = -2**31
DECIMAL_POINT = '.'
PERCENTAGE_SIGN = '%'

def myAtoi(s):
    state = 'start'
    sign = 1
    answer = 0
    decimal_count = 0
    fraction = 0

    table = {
        'start': ['start', 'signed', 'in_number', 'end', 'in_decimal', 'in_percentage'],
        'signed': ['end', 'end', 'in_number', 'end', 'in_decimal', 'end'],
        'in_number': ['end', 'end', 'in_number', 'end', 'end', 'end'],
        'end': ['end', 'end', 'end', 'end', 'end', 'end'],
        'in_decimal': ['end', 'end', 'in_decimal', 'end', 'end', 'in_percentage'],
        'in_percentage': ['end', 'end', 'end', 'end', 'end', 'end'],
    }

    def get_col(c):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        if c == DECIMAL_POINT:
            return 4
        if c == PERCENTAGE_SIGN:
            return 5
        return 3

    for c in s:
        state = table[state][get_col(c)]
        
        if state == 'in_number':
            answer = answer * 10 + int(c)
            answer = min(answer, INT_MAX) if sign == 1 else min(answer, -INT_MIN)
        elif state == 'signed':
            sign = 1 if c == '+' else -1
        elif state == 'in_decimal':
            decimal_count += 1
            fraction = fraction + int(c) * (10**-decimal_count)
        elif state == 'in_percentage':
            answer = answer / 100
            fraction = fraction / 100

    return int(sign * (answer + fraction))