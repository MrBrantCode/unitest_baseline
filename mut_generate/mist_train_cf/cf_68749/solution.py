"""
QUESTION:
Write a function `mutate_case_and_evolve_symbols` that takes a string as input and returns a modified string where: 
- all uppercase letters are converted to lowercase and vice versa, 
- odd digits are replaced by their next even number, 
- and specific special characters '!@#$%^&*()' are doubled.
"""

def mutate_case_and_evolve_symbols(string: str) -> str:
    result = ''
    for char in string:
        if char.isalpha():
            if char.islower():
                result += char.upper()
            else:
                result += char.lower()
        elif char.isdigit():
            if int(char) % 2 != 0:
                result += str(int(char) + 1)
            else:
                result += char
        elif char in '!@#$%^&*()':
            result += char * 2
        else:
            result += char
    return result