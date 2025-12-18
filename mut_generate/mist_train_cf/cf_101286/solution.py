"""
QUESTION:
Write a function `contains_letter(word, letters)` that takes a word and a list of letters as input. The function should return `False` if the word contains one or zero letters from the given list, and return a list of all the letters in the word that matched the given letters in the list if the word contains more than one letter from the given list. The function must create a table that lists all the letters in the word and the corresponding indices, select the indices of the matched letters from the given list, and use a loop to iterate through the selected indices to obtain the matched letters.
"""

def contains_letter(word, letters):
    # create a table that lists all the letters in the word and the corresponding indices
    indices = {}
    for i, c in enumerate(word):
        if c in indices:
            indices[c].append(i)
        else:
            indices[c] = [i]
    
    # select the indices of the matched letters from the given list
    selected_indices = []
    for c in letters:
        if c in indices:
            selected_indices.extend(indices[c])
    
    # return False if there is only one matching letter
    if len(selected_indices) < 2:
        return False
    
    # use a loop to iterate through the selected indices to obtain the matched letters
    matched_letters = []
    for i in selected_indices:
        matched_letters.append(word[i])
    
    # return an array of all the letters in the word that matched the given letters in the list
    return matched_letters