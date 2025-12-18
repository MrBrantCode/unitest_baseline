"""
QUESTION:
Write a function `process_dialog(dialog)` that takes a string of oral dialog as input and returns a string containing the most diverse set of alphanumeric characters from the dialog, arranged in descending lexicographical order. The function should ignore case differences and non-alphanumeric characters.
"""

def process_dialog(dialog):
    # remove spaces from dialog
    dialog = dialog.replace(" ", "")
    
    # convert all letters to lower case
    dialog = dialog.lower()
    
    # create an empty set (for uniqueness)
    char_set = set()
    
    # iterate over the dialog
    for char in dialog:
        # add alphanumeric characters only
        if char.isalnum():
            char_set.add(char)
    
    # convert set to list, sort in descending order and join to string
    sorted_str = "".join(sorted(list(char_set), reverse=True))
    
    return sorted_str