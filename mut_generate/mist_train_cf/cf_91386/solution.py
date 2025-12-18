"""
QUESTION:
Create a function named `capitalize_words` that capitalizes the first letter of each word in a given string, maintaining the original casing of the rest of the word, handling multiple whitespace characters between words, and ignoring leading and trailing whitespace. The input string can contain punctuation and special characters, and both lowercase and uppercase letters.
"""

def capitalize_words(string):
    # Remove leading and trailing whitespace
    string = string.strip()
    
    # Split the string into words using whitespace as the delimiter
    words = string.split()
    
    # Capitalize the first letter of each word while maintaining the original casing of the rest of the word
    capitalized_words = [word[0].upper() + word[1:] for word in words]
    
    # Join the words back together with whitespace as the delimiter
    capitalized_string = ' '.join(capitalized_words)
    
    return capitalized_string