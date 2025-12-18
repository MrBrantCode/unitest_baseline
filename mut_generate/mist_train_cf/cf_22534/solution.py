"""
QUESTION:
Create a function `generate_powerset(s)` that generates the powerset of a given set `s` without using recursion. The function should have a time complexity of O(2^N), where N is the length of the input set. The input set `s` is assumed to be a list of unique elements.
"""

def generate_powerset(s):
    powerset = [[]]  
    for elem in s:
        new_subsets = []
        for subset in powerset:
            new_subsets.append(subset + [elem])
        powerset.extend(new_subsets)
    return powerset