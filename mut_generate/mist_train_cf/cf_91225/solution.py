"""
QUESTION:
Create a function called `categorize_strings` that categorizes a given list of strings into three categories: 'short', 'medium', and 'long' based on their lengths. A string is considered 'short' if it has less than 5 characters, 'medium' if it has between 5 and 10 characters, and 'long' if it has more than 10 characters. The function should return the categorized strings.
"""

def categorize_strings(strings):
    categorized_strings = {"short": [], "medium": [], "long": []}
    
    for string in strings:
        length = len(string)
        
        if length < 5:
            category = "short"
        elif length <= 10:
            category = "medium"
        else:
            category = "long"
        
        categorized_strings[category].append(string)
    
    return categorized_strings