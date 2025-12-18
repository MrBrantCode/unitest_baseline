"""
QUESTION:
Create a function called `combine_lists_to_dictionary` that takes two lists of strings as input and returns a dictionary where the keys are the strings from the first list and the values are the strings from the second list. 

The function should ignore strings that contain special characters, remove any duplicate keys and keep only the first occurrence, and convert the values to uppercase. 

Additionally, the function should check for anagrams in the input lists and remove them before combining the lists into a dictionary. The function should also ensure that the keys in the resulting dictionary do not contain any whitespace characters. 

The input lists are guaranteed to have the same length.
"""

from collections import OrderedDict
import re

def remove_special_characters(string):
    return re.sub(r'\W+', '', string)

def check_for_anagrams(list1, list2):
    list1_no_special_chars = [remove_special_characters(string) for string in list1]
    list2_no_special_chars = [remove_special_characters(string) for string in list2]
    
    for i in range(len(list1_no_special_chars)):
        if sorted(list1_no_special_chars[i].lower()) == sorted(list2_no_special_chars[i].lower()):
            del list1[i]
            del list2[i]
    
    return list1, list2

def combine_lists_to_dictionary(list1, list2):
    list1, list2 = check_for_anagrams(list1, list2)
    
    dictionary = OrderedDict()
    for key, value in zip(list1, list2):
        key = remove_special_characters(key)
        if key and key not in dictionary and not key.isspace():
            dictionary[key] = value.upper()
    
    return dictionary