"""
QUESTION:
Write a function named `get_subsets` that takes a list as input and returns a list of all possible subsets of the input list using list comprehension and recursion, without using any external libraries or the built-in function `pow()`. The function should not have any additional inputs and should return all subsets, including the empty subset and the input list itself.
"""

def get_subsets(lst):
    # Base case: an empty set has one subset, the empty set
    if len(lst) == 0:
        return [[]]

    # Recursive case: get the subsets of the list without the first element
    subsets_without_first = get_subsets(lst[1:])

    # Include the first element in each of these subsets
    subsets_with_first = [ [lst[0]] + subset for subset in subsets_without_first]

    # The total subsets are those with and without the first element
    return subsets_with_first + subsets_without_first