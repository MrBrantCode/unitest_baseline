"""
QUESTION:
Write a Python function named `filter_and_sort_dictionaries` that takes in a list of dictionaries. This function should return a new list of dictionaries, where each dictionary only includes key-value pairs where the key starts with a vowel and the value is a list of integers with a sum of at least 50. The dictionaries in the new list should be sorted in descending order based on the sum of the integers in the value list.
"""

def filter_and_sort_dictionaries(list_of_dicts):
    new_list_of_dicts = []
    
    for dict in list_of_dicts:
        new_dict = {}
        
        for key, value in dict.items():
            if key[0].lower() in ['a', 'e', 'i', 'o', 'u'] and isinstance(value, list) and all(isinstance(x, int) for x in value):
                if sum(value) >= 50:
                    new_dict[key] = value
        
        if new_dict:
            new_list_of_dicts.append(new_dict)
    
    new_list_of_dicts.sort(key=lambda x: sum([sum(v) for v in x.values()]), reverse=True)
    
    return new_list_of_dicts