"""
QUESTION:
Write a function that returns a sequence (index begins with 1) of all the even characters from a string. If the string is smaller than two characters or longer than 100 characters, the function should return "invalid string". 

For example:
`````
"abcdefghijklm" --> ["b", "d", "f", "h", "j", "l"]
"a"             --> "invalid string"
`````
"""

def get_even_characters(input_string: str) -> str or list:
    if len(input_string) < 2 or len(input_string) > 100:
        return "invalid string"
    return [input_string[i] for i in range(1, len(input_string), 2)]