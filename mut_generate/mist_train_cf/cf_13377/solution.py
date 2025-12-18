"""
QUESTION:
Create a function `split_string` that takes a string and a character as input, splits the string on the character, and returns the resulting list. The function should treat consecutive occurrences of the character as a single delimiter and exclude empty strings from the resulting list. The function should not use any built-in string splitting functions or regular expressions.
"""

def split_string(string, char):
    result = []
    temp = ""
    prev_char = ""
    
    for i in range(len(string)):
        if string[i] == char:
            if prev_char != char:
                if temp != "":
                    result.append(temp)
                temp = ""
        else:
            temp += string[i]
        
        prev_char = string[i]
    
    if temp != "":
        result.append(temp)
    
    return result