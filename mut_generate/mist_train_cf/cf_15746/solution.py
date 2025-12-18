"""
QUESTION:
Write a function named `capitalize_words` that takes a string as input. The function should return the string with the first letter of each word capitalized and the rest of the word in lowercase. Remove any leading or trailing spaces from the string and reduce multiple spaces between words to a single space. Assume the input string only contains alphabetical characters and spaces.
"""

def capitalize_words(input_string):
    # Remove leading and trailing spaces
    input_string = input_string.strip()
    
    # Split the string into words
    words = input_string.split()
    
    # Capitalize the first letter of each word and convert the rest to lowercase
    words = [word.capitalize() for word in words]
    
    # Join the words with a single space
    output_string = " ".join(words)
    
    return output_string