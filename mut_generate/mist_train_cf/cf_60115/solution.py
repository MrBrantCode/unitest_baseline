"""
QUESTION:
Write a function `unique_sequence(strings)` that takes an array of strings as input and returns a dictionary where the keys are the distinct elements from the array and the values are lists containing the elements in their order of first occurrence after removing all duplications. The function should have a time complexity of O(n), where n is the number of elements in the input array.
"""

def unique_sequence(strings):
    sequence = {}
    recent = None
    for s in strings:
        if recent is not None and recent != s and s not in sequence[recent]:
            sequence[recent].append(s)
        if s not in sequence:
            sequence[s] = []
        recent = s
    return sequence