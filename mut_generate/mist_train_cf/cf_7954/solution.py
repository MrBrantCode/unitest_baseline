"""
QUESTION:
Write a function called `combine_and_filter` that takes two lists of strings as input and returns a list of unique strings that are palindromes. The function should consider alphanumeric characters only and ignore case. The function should also have a time complexity of O(n), where n is the total number of characters in all the strings combined.
"""

import re

def combine_and_filter(list1, list2):
    combined_list = list1 + list2
    
    # Create a set to store unique palindromes
    palindrome_set = set()
    
    for string in combined_list:
        # Remove non-alphanumeric characters and convert to lowercase
        clean_string = re.sub(r'[^a-zA-Z0-9]', '', string).lower()
        
        # Check if the string is a palindrome
        if clean_string == clean_string[::-1]:
            palindrome_set.add(string)
    
    # Convert the set back to a list
    palindrome_list = list(palindrome_set)
    
    return palindrome_list