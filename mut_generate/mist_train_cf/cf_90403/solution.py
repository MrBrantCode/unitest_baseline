"""
QUESTION:
Implement a function called `concatenate_strings` that takes two strings as input, combines them into one string in the given order, and stores the result in a separate string variable. The function must not use built-in string concatenation or joining functions. The final string should only contain unique characters from the original strings, be sorted in ascending order based on ASCII values of characters, and be reversed.
"""

def concatenate_strings(string1, string2):
    unique_chars = set()
    
    for char in string1:
        unique_chars.add(char)
    
    for char in string2:
        unique_chars.add(char)
    
    sorted_chars = sorted(unique_chars, key=lambda x: ord(x))
    
    final_string = ""
    for char in sorted_chars:
        final_string += char
    
    final_string = final_string[::-1]
    
    return final_string