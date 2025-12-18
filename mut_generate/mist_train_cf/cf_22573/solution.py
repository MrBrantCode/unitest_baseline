"""
QUESTION:
Write a function named `filter_dict` that takes a dictionary as input and returns a new dictionary. The new dictionary should only include key-value pairs from the input dictionary where the key starts with a vowel (a, e, i, o, or u) and the value is a list of integers. The function should exclude any key-value pairs where the sum of the integers in the value list is less than 10. The keys in the new dictionary should be sorted alphabetically.
"""

def filter_dict(dictionary):
    new_dict = {}
    vowels = ['a', 'e', 'i', 'o', 'u']
    for key, value in dictionary.items():
        if key[0].lower() in vowels and all(isinstance(x, int) for x in value):
            if sum(value) >= 10:
                new_dict[key] = value
    return dict(sorted(new_dict.items()))