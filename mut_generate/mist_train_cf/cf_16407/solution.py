"""
QUESTION:
Write a function called `compute_minkowski_distance` that calculates the Minkowski distance between two lists. The function takes three parameters: two lists `list1` and `list2` with up to 10^6 elements ranging from -10^9 to 10^9, and an integer `p` greater than 0. The function should return the Minkowski distance between the two lists, or an error message if the lists have different lengths or if `p` is not greater than 0.
"""

def compute_minkowski_distance(list1, list2, p):
    if len(list1) != len(list2):
        return "Lists must have the same length."
    
    if p == 0:
        return "p must be greater than 0."
    
    distance = 0
    for i in range(len(list1)):
        distance += abs(list1[i] - list2[i]) ** p
    
    return distance ** (1/p)