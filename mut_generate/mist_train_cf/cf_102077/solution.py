"""
QUESTION:
Write a function named `convert_dict_to_list` that takes a dictionary as input and returns a list of tuples. Each tuple in the list should contain a key-value pair from the input dictionary where the key starts with a vowel. The function should only include key-value pairs where the key starts with the letters 'a', 'e', 'i', 'o', or 'u'.
"""

def convert_dict_to_list(my_dict):
    vowel_list = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    for key, value in my_dict.items():
        if key[0].lower() in vowels:
            vowel_list.append((key, value))
    return vowel_list