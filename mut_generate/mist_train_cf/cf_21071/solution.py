"""
QUESTION:
Create a function `first_and_last_words` that takes an array of strings as input and returns an array of tuples, where each tuple contains the first and last word of each string. The function should ignore leading/trailing whitespace, handle multiple consecutive spaces, single-word strings, and remove punctuation marks (commas, periods, exclamation marks) from words. If the input array is empty, return an empty array.
"""

def first_and_last_words(strings):
    result = []
    
    for string in strings:
        string = string.strip()  
        
        if string == "":
            continue
            
        words = string.split()  
        first_word = words[0].strip(",.!")  
        last_word = words[-1].strip(",.!")  
        
        result.append((first_word, last_word))
        
    return result