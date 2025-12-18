"""
QUESTION:
Create a function `powerset` that generates the powerset of a given input set without using recursion. The function should have a time complexity of O(2^N), where N is the length of the input set. The function should also handle duplicate elements in the input set and return only unique subsets.
"""

def powerset(input_set):
    n = len(input_set)
    powerset = [[]]  

    for i in range(n):
        current_powerset_size = len(powerset)

        for j in range(current_powerset_size):
            subset = powerset[j]
            new_subset = subset + [input_set[i]]
            if new_subset not in powerset:
                powerset.append(new_subset)

    return powerset