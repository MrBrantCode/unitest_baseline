"""
QUESTION:
Develop a function named `advanced_sequence` that takes a list of strings as input, where each string contains either numbers or alphabets. The function should return 'Yes' if a correct reversing order exists, resulting in a string with correctly inverted sequences of both numbers and alphabets, and 'No' otherwise. The function must check if all substrings are individually letters and numbers, and if they are in decreasing order.
"""

def advanced_sequence(lst):
    strng = ''.join(lst)

    alphabets = []
    numbers = []
    
    for num_alpha in strng:
        if num_alpha.isalpha():
            alphabets.append(num_alpha)
            # check if 'numbers' list is in decreasing order
            if numbers and numbers != sorted(numbers, reverse=True):
                return 'No'
            numbers = [] # empty the list for next number sequence
        if num_alpha.isdigit():
            numbers.append(num_alpha)
            # check if 'alphabets' list in in decreasing order
            if alphabets and alphabets != sorted(alphabets, reverse=True):
                return 'No'
            alphabets = [] # empty the list for next alphabet sequence

    # handle the possible last sequence of numbers and alphabets
    if (numbers and numbers != sorted(numbers, reverse=True)) or \
       (alphabets and alphabets != sorted(alphabets, reverse=True)):
        return 'No'

    return 'Yes'