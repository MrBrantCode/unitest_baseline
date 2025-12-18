"""
QUESTION:
Create a function `merge_dictionaries` that takes two dictionaries as input and returns a new dictionary. The new dictionary should contain all keys that start with a vowel and have a value that is a multiple of 3. If a key is present in both input dictionaries, the value in the second dictionary should be used in the new dictionary. The original input dictionaries should not be modified.
"""

def merge_dictionaries(dictionary1, dictionary2):
    vowels = ['a', 'e', 'i', 'o', 'u']
    merged_dictionary = {}

    for key in set(dictionary1.keys()).union(dictionary2.keys()):
        if key[0].lower() in vowels and key in dictionary1 and key in dictionary2:
            if dictionary2[key] % 3 == 0:
                merged_dictionary[key] = dictionary2[key]
        elif key[0].lower() in vowels and key in dictionary1:
            if dictionary1[key] % 3 == 0:
                merged_dictionary[key] = dictionary1[key]
        elif key[0].lower() in vowels and key in dictionary2:
            if dictionary2[key] % 3 == 0:
                merged_dictionary[key] = dictionary2[key]
    
    return merged_dictionary