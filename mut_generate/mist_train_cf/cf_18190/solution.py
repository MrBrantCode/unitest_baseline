"""
QUESTION:
Create a function called `remove_characters` that takes a string as input and returns a new string with all non-alphanumeric characters removed, all letters converted to lowercase, and all duplicate characters removed, while maintaining a time complexity of O(n) and a space complexity of O(n).
"""

def remove_characters(s):
    cleaned_string = ""
    seen = set()
    
    for char in s:
        if char.isalnum():
            if char.isupper():
                char = char.lower()
            if char not in seen:
                cleaned_string += char
                seen.add(char)
    
    return cleaned_string