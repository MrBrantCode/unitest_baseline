"""
QUESTION:
Create a function `alter_string` that takes a string as input. For each character in the string, if the character is an alphabet, convert it to its ASCII value; if it's a digit and even, increase it by one; if it's a special character, quadruple it. Then, construct a dictionary where the keys are the altered characters and the values are their frequencies. The function should return a dictionary containing the altered string as the key and the frequency dictionary as the value.
"""

def alter_string(string: str) -> dict:
    """ For each given string, change all alphabet characters to their ASCII values, increase even digits by one, quadruple all special characters, and assemble a dictionary that indicates the frequency of each different character.
    """
    ascii_str = ""
    ascii_dict = dict()
    
    for char in string:
        if char.isalpha():
            ascii_str += str(ord(char))+":"
            ascii_dict[str(ord(char))] = ascii_dict.get(str(ord(char)), 0) + 1
        elif char.isdigit():
            if int(char) % 2 == 0:
                ascii_str += str(int(char) + 1) + ":"
                ascii_dict[str(int(char) + 1)] = ascii_dict.get(str(int(char) + 1), 0) + 1
            else:
                ascii_str += char + ":"
                ascii_dict[char] = ascii_dict.get(char, 0) + 1
        else:
            ascii_str += char * 4
            ascii_dict[char] = ascii_dict.get(char, 0) + 4
            
    # remove the trailing ":"
    ascii_str = ascii_str.rstrip(":")
    result = {ascii_str: ascii_dict}
     
    return result