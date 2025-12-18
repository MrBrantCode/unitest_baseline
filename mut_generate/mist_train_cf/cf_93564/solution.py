"""
QUESTION:
Create a function `replace_punctuation` that takes a string as input, replaces all punctuation marks with a space, and removes any consecutive spaces resulting from the replacement. The function should have a time complexity of O(n), where n is the length of the input string, and should not use built-in string manipulation functions like `replace()` or regex. The input string can have a maximum length of 10^6 characters.
"""

def replace_punctuation(string):
    # Create a set of all punctuation marks to be replaced
    punctuation_marks = {'.', ',', '!', '-', '...', '—', '–', '(', ')', '[', ']', '{', '}', ':', ';', '?', '/', '\\'}

    # Convert the string into a list of characters
    string_list = list(string)
    
    # Iterate through the list and replace punctuation marks with spaces
    for i in range(len(string_list)):
        if string_list[i] in punctuation_marks:
            string_list[i] = ' '
    
    # Convert the list back to a string
    new_string = ''.join(string_list)
    
    # Remove consecutive spaces resulting from the replacement
    new_string = ' '.join(new_string.split())
    
    return new_string