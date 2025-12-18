"""
QUESTION:
Write a function `sort_dict_by_values` that takes a dictionary as input. The function should return a new dictionary containing only the entries where the keys are strings that start with a vowel (a, e, i, o, or u) and have a value of at least 5. The returned dictionary should be sorted by values in descending order.
"""

def sort_dict_by_values(dictionary):
    vowel_start_keys = [key for key in dictionary.keys() if key[0].lower() in 'aeiou']
    filtered_dict = {key: value for key, value in dictionary.items() if value >= 5 and key in vowel_start_keys}
    return dict(sorted(filtered_dict.items(), key=lambda item: item[1], reverse=True))