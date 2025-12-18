"""
QUESTION:
Write a function `unique_vowel_values` that takes a list of tuples as input. The function should return a list of unique values from the list of tuples, based on the second element of each tuple, sorted alphabetically. However, it should only consider tuples where the first element starts with a vowel.
"""

def unique_vowel_values(my_list):
    unique_values = set()
    vowels = 'aeiou'
    for item in my_list:
        if item[0][0].lower() in vowels:
            unique_values.add(item[1])
    return sorted(list(unique_values))