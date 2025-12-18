"""
QUESTION:
Create a function named `star_transformer` that takes one string argument and returns a string where all digit characters and special characters (except for whitespace) are replaced with '*'. The function should not use any built-in Python string methods or libraries. The function should preserve the original whitespace and letters in the input string.
"""

def star_transformer(string):
    star_string = ''
    for i in string:
        if 'A'<=i<='Z' or 'a'<=i<='z' or i==' ':
            star_string += i 
        else:
            star_string += '*' 
    return star_string