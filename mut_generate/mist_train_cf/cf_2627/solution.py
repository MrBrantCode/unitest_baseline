"""
QUESTION:
Write a function `combinations(l1, l2)` that takes two lists `l1` and `l2` as input and returns a new list containing all unique combinations of elements from `l1` and `l2`. Each combination should be a string formed by concatenating one element from `l1` with one element from `l2`. The function should not use any built-in functions or libraries that directly solve this problem and should have a time complexity of O(n^2), where n is the length of the longer input list.
"""

def combination(l1, l2):
    result = []
    for elem1 in l1:
        for elem2 in l2:
            combination = str(elem1) + str(elem2)
            if combination not in result:
                result.append(combination)
    return result