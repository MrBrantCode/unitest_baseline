"""
QUESTION:
Write a function named `find_dissimilar` that takes two tuples as input and returns a dictionary where the keys are the dissimilar elements from the tuples and the values are tuples containing the count of the dissimilar element and a string indicating the originating tuple. If a dissimilar element is found in both tuples, the count from both tuples should be returned as a list in the format [count from tuple1, count from tuple2] and the string "both".
"""

def find_dissimilar(tup1, tup2):
    dissimilars = {}
    for t in tup1:
        if t in tup2:
            if t in dissimilars:
                dissimilars[t][0][0] += 1
            else:
                dissimilars[t] = [[1, tup2.count(t)], 'both']
        else:
            dissimilars[t] = [tup1.count(t), 'tuple1']

    for t in tup2:
        if t not in tup1 and t not in dissimilars:
            dissimilars[t] = [tup2.count(t), 'tuple2']
 
    return dissimilars