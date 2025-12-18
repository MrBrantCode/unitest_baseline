"""
QUESTION:
Create a function named `powerset` that generates all possible subsets of a given set without using recursion. The function should take one argument, a list of elements, and return a list of lists where each sublist is a subset of the input set. The function should not use recursion to generate the subsets.
"""

def powerset(s):
    n = len(s)
    powerset = [[]]

    for i in range(n):
        subsets = []
        for subset in powerset:
            subsets.append(subset + [s[i]])
        powerset += subsets

    return powerset