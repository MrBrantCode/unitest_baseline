"""
QUESTION:
Create a function named `capitalize_string` that takes a string of any length as input, splits it into words, and returns a new string where the first letter of each word is capitalized.
"""

def capitalize_string(string):
    words = string.split()  
    capitalized_words = [word.capitalize() for word in words]  
    capitalized_string = " ".join(capitalized_words)  
    return capitalized_string