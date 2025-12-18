"""
QUESTION:
Write a function `format_strings` that takes a list of strings as input and returns a new list where each string has only the first letter of each word capitalized and the remaining letters in uppercase. The solution should have a time complexity of O(n) and a space complexity of O(1).
"""

def format_strings(strings):
    formatted_strings = []
    
    for string in strings:
        words = string.split()
        formatted_words = []
        
        for word in words:
            formatted_word = word[0].upper() + word[1:].lower()
            formatted_words.append(formatted_word)
        
        formatted_string = ' '.join(formatted_words)
        formatted_strings.append(formatted_string)
    
    return formatted_strings