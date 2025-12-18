"""
QUESTION:
Create a function called `first_and_last_words` that takes an array of strings as input and returns an array of tuples. Each tuple should contain the first and last word of the corresponding input string. The function should ignore leading/trailing whitespace, remove punctuation marks (",", ".", "!") from the words, and handle cases where a string contains multiple consecutive spaces or only one word. If the input array is empty, the function should return an empty array.
"""

def first_and_last_words(strings):
    result = []
    
    for string in strings:
        string = string.strip()  # Remove leading and trailing whitespace
        
        if string == "":  # Ignore empty strings
            continue
            
        words = string.split()  # Split string into words
        first_word = words[0].strip(",.!")  # Remove punctuation marks from first word
        last_word = words[-1].strip(",.!")  # Remove punctuation marks from last word
        
        result.append((first_word, last_word))
        
    return result