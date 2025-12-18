"""
QUESTION:
Implement a function `remove_short_words` that takes a string as input, removes words with less than 5 characters, replaces "hello" with "goodbye", and reverses the order of the words. The input string only contains alphabetical characters and spaces, with single spaces between words. The output should have a single space between words and consider leading or trailing spaces.
"""

def remove_short_words(string: str) -> str:
    # Remove leading and trailing spaces
    string = string.strip()
    
    # Split the string into a list of words
    words = string.split()
    
    # Remove words that have less than 5 characters and replace "hello" with "goodbye"
    words = [word.replace("hello", "goodbye") for word in words if len(word) >= 5]
    
    # Reverse the order of the words
    words = words[::-1]
    
    # Join the words with a single space
    modified_string = " ".join(words)
    
    return modified_string