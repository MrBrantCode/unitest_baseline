"""
QUESTION:
Create a function named `convert_list_to_dict` that takes a list of alternating numbers and letters as input. The function should return a dictionary where the keys are the numbers and the values are lists of corresponding letters. If a number appears multiple times in the input list, the corresponding value in the dictionary should be a list of letters sorted in descending order based on their ASCII values.
"""

def convert_list_to_dict(lst):
    dictionary = {}
    for i in range(0, len(lst), 2):
        number = lst[i]
        letter = lst[i+1]
        if number in dictionary:
            dictionary[number].append(letter)
            dictionary[number].sort(reverse=True, key=lambda x: ord(x))
        else:
            dictionary[number] = [letter]
    return dictionary