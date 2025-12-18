"""
QUESTION:
Write a function called `is_anagram` that takes two string parameters, `str1` and `str2`, and returns a boolean indicating whether these two strings are anagrams of each other, ignoring case and whitespace differences.
"""

def is_anagram(str1, str2):
    # removing all whitespace from strings 
    str1 = ''.join(str1.split())
    str2 = ''.join(str2.split()) 

    # create list for each string 
    list_str1 = list(str1.upper()) 
    list_str2 = list(str2.upper()) 

    # sort the list 
    list_str1.sort() 
    list_str2.sort() 

    # checking if both lists are identical or not 
    return list_str1 == list_str2