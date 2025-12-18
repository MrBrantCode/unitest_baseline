"""
QUESTION:
Write a function called `filter_list` that takes a list of strings as input. The function should remove any strings that start with 'S' and end with a vowel, and any strings containing numbers or special characters. It should also remove duplicate strings from the list. The function should return the filtered list.
"""

def filter_list(lst):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_list = []
    for word in lst:
        if word[0].lower() == 's' and word[-1].lower() in vowels:
            continue
        if any(char.isdigit() or not char.isalnum() for char in word):
            continue
        if word not in filtered_list:
            filtered_list.append(word)
    return filtered_list