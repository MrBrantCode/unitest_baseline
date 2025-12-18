"""
QUESTION:
Create a function called `title_case` that takes a string as input. The function should format the string into proper title case, correctly capitalizing the first letter of each word except for certain words that should remain lowercase, such as articles, prepositions, and conjunctions. The function should handle edge cases such as empty strings and strings with leading/trailing spaces. The function should have a time complexity of O(n), where n is the length of the input string, and a space complexity of O(1), without using any additional data structures or variables that scale with the size of the input string.
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