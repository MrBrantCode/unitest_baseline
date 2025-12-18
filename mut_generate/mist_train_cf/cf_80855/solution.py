"""
QUESTION:
Create a function `transform_text` that takes a string `input_string` as input and returns a new string where the case of each character is alternated. The first character should be in uppercase, the second in lowercase, the third in uppercase, and so on.
"""

def transform_text(input_string):
    new_string = ""
    index = 0
  
    for char in input_string:
        if index % 2 == 0:
            new_string += char.upper()
        else:
            new_string += char.lower()
        
        index += 1
  
    return new_string