"""
QUESTION:
Create a function `flip_case_and_modify` that takes a string as input and returns a modified string where:
- Alphabetic letters have their case inverted (lowercase becomes uppercase and vice versa)
- Odd digits are replaced with the next even digit
- All other characters (symbols) are duplicated.
"""

def flip_case_and_modify(string: str) -> str:
    result = []

    for char in string:
        if char.isdigit():
            if int(char) % 2 != 0:
                result.append(str(int(char) + 1))
            else:
                result.append(char)
        elif char.isalpha():
            if char.islower():
                result.append(char.upper())
            else:
                result.append(char.lower())
        else:
            result.append(char * 2)

    return ''.join(result)