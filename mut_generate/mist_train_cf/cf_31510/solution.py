"""
QUESTION:
Implement a function `categorize_by_first_letter(categories)` that takes a list of strings representing categories as input. The function should return a dictionary where the keys are the first letters of the categories (both uppercase and lowercase considered as the same) and the values are lists of categories starting with the corresponding letter.
"""

def entrance(categories):
    categorized_dict = {}
    for category in categories:
        first_letter = category[0].upper()
        if first_letter not in categorized_dict:
            categorized_dict[first_letter] = [category]
        else:
            categorized_dict[first_letter].append(category)
    return categorized_dict