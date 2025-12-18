"""
QUESTION:
Write a function named title_case that takes a string as input, formats it in proper title case, and returns the formatted string. The function should correctly capitalize the first letter of each word in the string, except for certain words (articles, prepositions, conjunctions) that should be lowercase. The function should also handle edge cases such as empty strings and strings with leading/trailing spaces. The function should have a time complexity of O(n), where n is the length of the input string, and a space complexity of O(1), meaning it should not use any additional data structures or variables that scale with the size of the input string.
"""

def title_case(string):
    if not string:
        return string
    
    string = string.strip()
    lowercase_words = ['a', 'an', 'the', 'and', 'but', 'for', 'or', 'nor', 'on', 'at', 'to', 'from', 'by', 'in', 'of']
    
    # Convert the string to lowercase
    string = string.lower()
    
    # Create a list of words in the string
    words = string.split()
    
    # Capitalize the first letter of each word, except for certain lowercase words
    for i in range(len(words)):
        if i == 0 or words[i] not in lowercase_words:
            words[i] = words[i].capitalize()
    
    # Join the words back together and return the formatted string
    return ' '.join(words)