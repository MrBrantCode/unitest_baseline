"""
QUESTION:
Create a function named `capitalize_sentence` that takes a string of lowercase letters and spaces as input. The string should be at least one character long but not exceed 100 characters. The function should return a string where the first letter of each word is capitalized and the rest of the letters are in lowercase.
"""

def capitalize_sentence(sentence):
    words = sentence.split()  
    capitalized_words = [word.capitalize() for word in words]  
    capitalized_sentence = " ".join(capitalized_words)  
    return capitalized_sentence