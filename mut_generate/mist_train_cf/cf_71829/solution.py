"""
QUESTION:
Write a function `find_strings(list1, list2, chosen)` that takes two distinct lists of strings and a chosen string from one of the lists as input, and returns the indices of two strings, one from each list, whose combined length equals the length of the chosen string. The function should find a unique solution without using the same string twice.
"""

def find_strings(list1, list2, chosen):
    # Find the length of the chosen string
    chosen_len = len(chosen)
   
    # Loop over the lists
    for i in range(len(list1)):
            for j in range(len(list2)):
                # Check if the combined length of the strings equals the length of the chosen string
                if len(list1[i]) + len(list2[j]) == chosen_len:
                    return [i, j]