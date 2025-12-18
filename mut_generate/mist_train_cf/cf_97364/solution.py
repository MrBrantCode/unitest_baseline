"""
QUESTION:
Create a function named `count_characters` that takes a string as input and returns a dictionary containing the number of occurrences of each alphanumeric character and whitespace in the string. The function should handle both uppercase and lowercase letters, convert all letters to lowercase, and consider whitespace characters. The output dictionary should be sorted in ascending order of the characters' ASCII values.
"""

def count_characters(text):
    char_counts = {}
    
    for char in text:
        if char.isalnum() or char.isspace():
            char = char.lower()
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
                
    sorted_char_counts = dict(sorted(char_counts.items(), key=lambda x: ord(x[0])))
    return sorted_char_counts