"""
QUESTION:
Create a function named `reverse_capitalize_words` that takes an array of strings as input. For each string, ignore it if it contains any digits. Otherwise, split the string into individual words, reverse and capitalize each word if it consists solely of letters, and join the processed words into a single string separated by commas. Finally, join the processed strings into a single output separated by commas.
"""

def reverse_capitalize_words(strings):
    result = []
    for string in strings:
        if any(char.isdigit() for char in string):
            continue
        
        words = string.split()
        reversed_words = []
        for word in words:
            if word.isalpha():
                reversed_words.append(word[::-1].capitalize())
        
        result.append(', '.join(reversed_words))
    
    return ', '.join(result)