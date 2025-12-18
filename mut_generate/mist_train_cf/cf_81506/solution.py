"""
QUESTION:
Write a function `sort_and_group` that takes a dictionary of linguistic terms and their definitions as input. The function should return a dictionary where the terms are ordered in increasing alphabetical order, each term is followed by its definition, and the terms are grouped based on their first letter. 

Restrictions: The input dictionary keys are the linguistic terms and the corresponding values are the definitions. The output dictionary should have the first letter of each term as the key and a list of tuples, where each tuple contains a term and its definition, as the value.
"""

def sort_and_group(words):
    sorted_words = sorted(words.items())
    result_dict = {}
    for word, definition in sorted_words:
        first_letter = word[0]
        if first_letter in result_dict:
            result_dict[first_letter].append((word,definition))
        else:
            result_dict[first_letter] = [(word,definition)]
    return result_dict