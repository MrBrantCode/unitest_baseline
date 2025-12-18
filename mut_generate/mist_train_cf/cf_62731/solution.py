"""
QUESTION:
Create a function named `filter_words` that takes a list of strings as input and returns a list of words. The returned list should include only the words that have more than 5 characters in length, contain only alphabetic characters, and are not null or empty. The function should be case insensitive, treating all words in lowercase.
"""

def filter_words(full_list):
    # Ensure all elements are strings
    full_list = [str(i) for i in full_list]

    word_list = [i for i in full_list 
        if len(i) > 5 and 
        i.isalpha() and 
        i != 'null' and 
        i.strip() != '']
    
    # Convert the words into lowercase
    word_list = [i.lower() for i in word_list]
    
    return word_list