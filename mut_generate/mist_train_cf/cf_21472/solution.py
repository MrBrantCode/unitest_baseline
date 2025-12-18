"""
QUESTION:
Write a function `is_anagram(str1, str2)` that takes two strings as input and returns `True` if they are anagrams of each other, ignoring case and spaces, and `False` otherwise. The function should handle exceptions where either input string is `None` and any memory errors that may occur during the comparison process.
"""

def is_anagram(str1, str2):
    try:
        # Check if either input string is None
        if str1 is None or str2 is None:
            return False
        
        # Remove any spaces and convert both strings to lowercase
        str1 = str1.replace(" ", "").lower()
        str2 = str2.replace(" ", "").lower()
        
        # Check if the lengths of the strings are different
        if len(str1) != len(str2):
            return False
        
        # Convert the strings to lists and sort them
        str1_list = sorted(list(str1))
        str2_list = sorted(list(str2))
        
        # Compare the sorted lists
        if str1_list == str2_list:
            return True
        else:
            return False
    
    # Handle any possible memory errors
    except MemoryError:
        print("Memory error occurred.")
        return False