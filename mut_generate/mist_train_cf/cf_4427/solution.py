"""
QUESTION:
Create a function called `search_strings` that takes in an array of strings and a search term. The function should return an array of indices of strings that match the search term in a case-insensitive manner, considering partial matches and including only the first occurrence of each partial match. The indices in the output array should correspond to the strings in the input array where the search term is found.
"""

def search_strings(array, search_term):
    indices = []
    for i in range(len(array)):
        if search_term.lower() in array[i].lower():
            indices.append(i)
    return indices