"""
QUESTION:
Write a function called `count_unique_characters` that takes a string as input and returns the number of unique characters in the string without using any additional data structures. The function should not use any data structures like lists, dictionaries, sets, or tuples other than the input string itself.
"""

def count_unique_characters(string):
    characters = list(string)
    non_unique_count = 0
    
    for i in range(len(characters)):
        if characters[i] == '':
            continue
        
        for j in range(i+1, len(characters)):
            if characters[i] == characters[j]:
                characters[j] = ''
                non_unique_count += 1
       
    unique_count = len(characters) - non_unique_count
    
    return unique_count