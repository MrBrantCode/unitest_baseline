"""
QUESTION:
Write a function `compute_minkowski_distance(list1, list2, p)` that calculates the Minkowski distance between two lists, `list1` and `list2`, with a given order `p`. The lists can contain up to 10^6 elements, and each element can range from -10^9 to 10^9. The function should return an error message if the lists have different lengths or if `p` is not greater than 0.
"""

def compute_minkowski_distance(list1, list2, p):
    if len(list1) != len(list2):
        return "Lists must have the same length."
    
    if p <= 0:
        return "p must be greater than 0."
    
    distance = 0
    for i in range(len(list1)):
        distance += abs(list1[i] - list2[i]) ** p
    
    return distance ** (1/p)