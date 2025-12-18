"""
QUESTION:
Create a function called `ascii_4th_char` that takes a text string as input and returns a string containing the ASCII values of every fourth character, starting from the index of 3, with any digit characters replaced with their corresponding Roman numerals. If the input string length is less than 4, the function should return "Index out of range".
"""

def ascii_4th_char(s):
    out = ""
    l = len(s)
    for i in range(3, l, 4):
        if s[i].isdigit():
            mapping = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
            out += mapping[int(s[i])-1]
        else:
            out += str(ord(s[i]))
    return out if out else "Index out of range"