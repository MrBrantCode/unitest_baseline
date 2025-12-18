"""
QUESTION:
Write a function `find_dissimilar(t1, t2)` that takes two tuples `t1` and `t2` as input. The function should return a dictionary where the keys are the dissimilar elements in `t1` and `t2`, and the values are tuples containing the counts of these elements in both tuples and the tuple identifier (1 or 2) from which the dissimilar element originated. For elements found in both tuples, return the count from both tuples separately.
"""

def find_dissimilar(t1, t2):
    d1, d2 = {}, {}
    for el in t1:
        if el not in t2:
            d1[el] = (d1.get(el, (0,0))[0] + 1, 1)
    for el in t2:
        if el not in t1:
            d2[el] = (d2.get(el, (0,0))[0] + 1, 2)
    result = {**d1, **d2}
    common = set(t1) & set(t2)
    for el in common:
        result[el] = (t1.count(el), t2.count(el))
    return result