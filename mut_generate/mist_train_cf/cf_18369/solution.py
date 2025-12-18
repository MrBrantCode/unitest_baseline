"""
QUESTION:
Create a function `is_valid_isbn_10` and `is_valid_isbn_13` to validate ISBN 10 and ISBN 13 codes, respectively. Each function should take a string `code` as input, strip leading and trailing spaces, and remove hyphens. The functions should check the length and format of the code, calculate the checksum digit based on the given algorithm, and return `True` if the code is valid and `False` otherwise. For ISBN 10 codes, the length should be 10, the first 9 characters should be digits, and the last character should be a digit or 'X'. For ISBN 13 codes, the length should be 13 and all characters should be digits.
"""

def is_valid_isbn_10(code):
    code = code.strip().replace('-', '')
    if len(code) != 10 or not code[:-1].isdigit() or not (code[-1].isdigit() or code[-1] == 'X'):
        return False
    checksum = sum((i+1) * int(x) if x.isdigit() else 10 for i, x in enumerate(code[:-1]))
    return str(checksum % 11) == code[-1]

def is_valid_isbn_13(code):
    code = code.strip().replace('-', '')
    if len(code) != 13 or not code.isdigit():
        return False
    checksum = sum(int(x) * (1 if i % 2 == 0 else 3) for i, x in enumerate(code[:-1]))
    return str((10 - (checksum % 10)) % 10) == code[-1]