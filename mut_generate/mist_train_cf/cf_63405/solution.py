"""
QUESTION:
Write a function named `convert_to_leet` that takes a string as input and returns the string converted to leetspeak. The conversion should be case-insensitive and include the following mappings: 'A' to '4', 'B' to '8', 'E' to '3', 'G' to '6', 'I' to '1', 'L' to '1', 'O' to '0', 'S' to '5', 'T' to '7', and 'Z' to '2'. Any characters not in these mappings should remain unchanged.
"""

def convert_to_leet(s):
    leet_dict = {'A':'4', 'B':'8', 'E':'3', 'G':'6', 'I':'1', 'L':'1', 'O':'0', 'S':'5', 'T':'7', 'Z':'2'}
    leet_string = ""
    for char in s:
        if char.upper() in leet_dict:
            leet_string += leet_dict[char.upper()]
        else:
            leet_string += char
    return leet_string