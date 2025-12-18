"""
QUESTION:
Create a function `remove_duplicates_and_sort` that takes a string as input. The function should remove duplicate characters from the string and return the output in a sorted order based on the ASCII values of the characters.
"""

def remove_duplicates_and_sort(string):
    # Convert the string into a set to remove duplicate characters
    unique_chars = set(string)
    
    # Convert the set back into a list to make it sortable
    unique_chars_list = list(unique_chars)
    
    # Use the sorted function to sort the list in ascending order based on the ASCII values of the characters
    sorted_chars_list = sorted(unique_chars_list)
    
    # Convert the sorted list back into a string using the join method
    output = "".join(sorted_chars_list)
    
    return output