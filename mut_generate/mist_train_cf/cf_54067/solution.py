"""
QUESTION:
Create a function named `flip_case_and_modify` that takes a string as input and returns a new string. The function should: 
- toggle the case of alphabetic characters (i.e., lowercase becomes uppercase and vice versa), 
- replace odd digits with the next even digit, and 
- duplicate special characters (i.e., non-alphanumeric characters).
"""

def flip_case_and_modify(string: str) -> str:
    """ For a given string, toggle lowercase characters to uppercase and vice versa, replace odd integers with the following even integer, and double special characters."""
    
    result = []
    
    for char in string:
        if char.isalpha():
            result.append(char.swapcase())
        elif char.isdigit():
            if int(char) % 2 != 0:
                result.append(str(int(char) + 1))
            else:
                result.append(char)
        elif not char.isalnum():
            result.append(char * 2)
            
    return ''.join(result)