"""
QUESTION:
Create a function called `flip_case_and_modify` that takes a string as input. Within the string, reverse the case of alphabetical letters (i.e., convert lowercase to uppercase and uppercase to lowercase), substitute odd digits with the subsequent even digit, and duplicate special characters. The function should return the modified string.
"""

def flip_case_and_modify(string: str) -> str:
    result = ""
    for char in string:
        if char.isalpha():
            result += char.swapcase()
        elif char.isdigit() and int(char) % 2 != 0:
            result += str(int(char) + 1)
        elif not char.isalnum():
            result += char * 2
        else:
            result += char
    return result