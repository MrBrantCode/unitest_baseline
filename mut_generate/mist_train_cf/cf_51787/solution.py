"""
QUESTION:
Create a function named `calc_sums` that takes two lists of numeric values as input and returns a comprehensive list containing all possible summations of pairs of numbers, one from each list. The function should iterate through each item in the first list and add it to each item in the second list, returning the results in a single list.
"""

def calc_sums(list1, list2):
    results = []
    for n1 in list1:
        for n2 in list2:
            results.append(n1+n2)
    return results