"""
QUESTION:
Create a function `capitalize_words(string)` that capitalizes the first letter of each word in a given string, maintaining the original letter casing of the rest of the word. The function should handle multiple whitespace characters between words, ignore leading and trailing whitespace, and support strings containing punctuation, special characters, and both lowercase and uppercase letters.
"""

def capitalize_words(string):
    string = string.strip()
    words = string.split()
    capitalized_words = [word[0].upper() + word[1:] for word in words]
    capitalized_string = ' '.join(capitalized_words)
    return capitalized_string