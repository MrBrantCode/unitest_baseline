"""
QUESTION:
Create a function called `sort_string_descending` that takes a string as input, sorts all characters in the string alphabetically in descending order, and returns the sorted string. The function should be implemented in Python and should not use any external libraries or built-in functions that directly sort in descending order.
"""

def sort_string_descending(string):
    # Convert string to a list of characters
    characters = list(string)
    
    # Sort the list of characters in ascending order
    sorted_characters = sorted(characters)
    
    # Reverse the sorted list
    sorted_characters.reverse()
    
    # Convert the list back to a string
    sorted_string = ''.join(sorted_characters)
    
    return sorted_string