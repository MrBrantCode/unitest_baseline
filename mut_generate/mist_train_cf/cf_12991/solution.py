"""
QUESTION:
Create a function `capitalize_words_except_specific_words` that capitalizes all words in a given string except for 'and' and 'the', regardless of their case in the original string. The function should return the modified string.
"""

def capitalize_words_except_specific_words(string):
    words = string.split()  
    capitalized_words = []  

    for word in words:
        if word.lower() in ["and", "the"]:  
            capitalized_words.append(word)  
        else:
            capitalized_words.append(word.capitalize())  

    return ' '.join(capitalized_words)  