"""
QUESTION:
Create a function named `count_characters` that takes a string as input, which contains only lowercase alphabets and has a length between 1 and 1000 characters. The function should return a dictionary where each key is a unique character from the input string and its corresponding value is the number of occurrences of that character. Implement this function without using any built-in Python functions or libraries for counting occurrences or creating dictionaries, and without using any loops.
"""

def count_characters(string):
    character_counts = {}

    def update_counts(string):
        if len(string) == 0:
            return
        
        character = string[0]
        
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1
        
        update_counts(string[1:])
    
    update_counts(string)
    
    return character_counts