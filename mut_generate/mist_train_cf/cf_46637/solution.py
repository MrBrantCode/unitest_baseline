"""
QUESTION:
Construct a function `uncommon_elements(sequence)` that takes a non-empty list of positive integers as input and returns a list of distinct integers with a frequency exceeding half the integer's value. The frequency of an integer is its occurrence count in the list. If no values meet this criterion, return an empty list.
"""

def uncommon_elements(sequence):
    '''
    Given a non-empty list of positive integers, return all distinct integers with a frequency exceeding half the integer's value.
    The frequency of an integer denotes its occurrence count in the list.
    If no values meet this criterion, return an empty list.
    '''
    frequency = {}
    result = []

    for element in sequence:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1

    for key, value in frequency.items():
        if value > (key / 2):
            result.append(key)

    return result