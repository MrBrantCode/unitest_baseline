"""
QUESTION:
Create a function that takes an input String and returns a String, where all the uppercase words of the input String are in front and all the lowercase words at the end.
The order of the uppercase and lowercase words should be the order in which they occur.

If a word starts with a number or special character, skip the word and leave it out of the result. 

Input String will not be empty.

For an input String: "hey You, Sort me Already!" 
the function should return: "You, Sort Already! hey me"
"""

def sort_words_by_case(input_string: str) -> str:
    # Split the input string into words
    words = input_string.split()
    
    # Filter out words that start with uppercase letters
    uppercase_words = [word for word in words if word[0].isupper()]
    
    # Filter out words that start with lowercase letters
    lowercase_words = [word for word in words if word[0].islower()]
    
    # Join the filtered words into a single string
    result = ' '.join(uppercase_words + lowercase_words)
    
    return result