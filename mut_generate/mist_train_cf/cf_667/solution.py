"""
QUESTION:
Create a function named `construct_dictionary` that takes a list of integers as input. The function should return a dictionary where the keys are the integers in the range from 1 to 1000 (inclusive) and the values are the corresponding lowercase letters from the English alphabet, with 'z' as the default value for keys not present in the input list.
"""

def construct_dictionary(given_list):
    dictionary = {}
    alphabet = [chr(x) for x in range(97, 123)]

    for i in range(1, 1001):
        if i in given_list:
            dictionary[i] = alphabet[i-1]
        else:
            dictionary[i] = 'z'
    return dictionary