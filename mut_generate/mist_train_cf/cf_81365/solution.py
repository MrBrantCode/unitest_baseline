"""
QUESTION:
Create a function named `process_personal_data` that takes a list of dictionaries as input, where each dictionary contains personal data attributes such as 'name', 'age', and 'city'. The function should handle dictionaries with missing keys and return a list of tuples, where each tuple contains the personal data attributes for one individual, with 'Unknown' as the default value for missing keys.
"""

def process_personal_data(dict_list):
    result = []
    for dic in dict_list:
        name = dic.get('name', 'Unknown')
        age = dic.get('age', 'Unknown')
        city = dic.get('city', 'Unknown')
        result.append((name, age, city))
    return result