"""
QUESTION:
Create a function `filter_list` that takes a list of strings as input and returns a new list with the following filters applied: 
1. Remove strings that start with 'S' and end with a vowel.
2. Remove strings that contain numbers or special characters.
"""

def filter_list(lst):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_lst = []
    for word in lst:
        if word[0].lower() == 's' and word[-1].lower() in vowels:
            continue
        if any(char.isdigit() or not char.isalnum() for char in word):
            continue
        filtered_lst.append(word)
    return filtered_lst