"""
QUESTION:
Define a function called `modify_string` that takes a list of strings (`str_list`) and a list of vowels as inputs. The function should return a dictionary where keys are the original strings and values are the modified strings with all the instances of vowels (both lower and uppercase) removed. If the string doesn't contain any of the provided vowels, return the string as it is. If a string becomes empty after removing vowels, its value in the dictionary should be `None`.
"""

def modify_string(str_list, vowels):
    result = {}
    for string in str_list:
        modified_string = ""
        for ch in string:
            if ch.lower() not in vowels:
                modified_string += ch
        result[string] = modified_string if modified_string else None
    return result