"""
QUESTION:
Write a function `filter_and_sort_dictionaries` that takes a list of dictionaries as input and returns a new list of dictionaries. The function should filter each dictionary to only include key-value pairs where the key starts with a vowel and the value is a list of integers with a sum greater than or equal to 50. The function should then sort the filtered dictionaries based on the sum of the integers in the value list in descending order.
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
    
    new_list_of_dicts.sort(key=lambda x: sum(sum(v) for v in x.values()), reverse=True)
    
    return new_list_of_dicts