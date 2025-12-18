"""
QUESTION:
Create a Python function named "find_common_characters" that takes two string parameters and returns a dictionary containing the shared characters (ignoring case) as keys and their total occurrences in both strings as values. The function should not use built-in functions like Counter.
"""

def find_common_characters(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    dict1 = {}
    dict2 = {}
    common_dict = {}
    
    # Iterating over each character in str1 and str2 to find the frequency count
    for char in str1:
        if char not in dict1:
            dict1[char] = 1
        else:
            dict1[char] += 1
            
    for char in str2:
        if char not in dict2:
            dict2[char] = 1
        else:
            dict2[char] += 1
            
    # Checking common keys in dict1 and dict2 and adding their values
    for key in dict1:
        if key in dict2:
            common_dict[key] = dict1[key] + dict2[key]
            
    return common_dict