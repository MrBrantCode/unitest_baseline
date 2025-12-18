"""
QUESTION:
Write a function `compare_sentences(s1, s2)` that compares two input sentences `s1` and `s2` and returns a dictionary. The dictionary should contain characters that appear in the same positions in both sentences as keys, with their respective counts as values. The function should be case-sensitive and ignore any characters beyond the length of the shorter sentence.
"""

def compare_sentences(s1, s2):
    # Initialize an empty dictionary
    result = {}
    
    # Convert both sentences to lists
    lst1 = list(s1)
    lst2 = list(s2)

    # Determine the minimum length of the two lists
    min_len = min(len(lst1), len(lst2))

    # Iterate over the lists up to the minimum length
    for i in range(min_len):
        # If the characters at the current position are the same...
        if lst1[i] == lst2[i]:
            # If the character is already a key in the dictionary, increment its value; else, add it with a value of 1
            result[lst1[i]] = result.get(lst1[i], 0) + 1
            
    # Return the resulting dictionary
    return result