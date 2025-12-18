"""
QUESTION:
Create a function named `sort_unique_elements` that takes a string of lowercase alphabets as input and returns a sorted array of unique elements in descending order. The function should have a time complexity of O(n log n) and a space complexity of O(n), where n is the length of the input string. The input string is guaranteed to contain only lowercase alphabets and have a maximum length of 10^5.
"""

def sort_unique_elements(input_string):
    # Convert the input string into a list of characters
    char_list = list(input_string)
    
    # Sort the list in ascending order
    char_list.sort()
    
    # Remove any duplicate elements from the list
    unique_list = list(set(char_list))
    
    # Sort the list in descending order
    unique_list.sort(reverse=True)
    
    # Return the sorted and unique list
    return unique_list