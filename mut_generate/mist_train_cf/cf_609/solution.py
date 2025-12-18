"""
QUESTION:
Write a function named `filter_list` that takes a list of strings as input and returns a new list after applying the following filters: 
- Remove strings starting with 'S' and ending with a vowel.
- Remove strings containing numbers or special characters.
- Remove duplicate strings from the list.
"""

def filter_list(lst):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_list = []

    for word in lst:
        if word[0] != 'S' or word[-1].lower() not in vowels:
            if not any(char.isdigit() or not char.isalpha() for char in word):
                if word not in filtered_list:
                    filtered_list.append(word)

    return filtered_list