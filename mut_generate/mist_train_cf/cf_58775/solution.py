"""
QUESTION:
Create a function `adjust_case_and_alter` that takes a string as input and returns a modified string. The function should invert the casing of all alphabetic characters (i.e., lowercase becomes uppercase and vice versa), replace any odd digits with their next even digit, and duplicate any special symbols (non-alphanumeric characters). The function should not alter any even digits.
"""

def adjust_case_and_alter(string: str) -> str:
    result = ""
    for character in string:
        if character.isalpha():  
            if character.isupper():  
                result += character.lower()  
            else:  
                result += character.upper()  
        elif character.isdigit():  
            if int(character) % 2 != 0:  
                result += str(int(character) + 1)  
            else:  
                result += character
        else:  
            result += character * 2  
    return result