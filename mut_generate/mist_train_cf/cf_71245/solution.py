"""
QUESTION:
Develop a function 'detectDupes' that takes a tuple 'T' as input and returns a dictionary where the keys are the duplicate elements in 'T' and the values are their respective counts. The function should work for tuples with elements of any type, including strings and integers.
"""

def detectDupes(T):
    dictionary = {}
    for char in T:
        if T.count(char) > 1:
            dictionary[char] = T.count(char)
    return dictionary