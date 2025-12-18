"""
QUESTION:
Write a function named `tuple_operations` that takes three tuples as input: `t1` and `t2` containing integers, and `ops` containing a set of operations. Perform the operations on `t1` and `t2` in the order they appear in `ops`, which can be "union", "intersection", "difference", or "symmetric_difference". Return the result of each operation in sorted order. If the "difference" operation cannot be performed because `t1` is a subset of `t2`, or if an invalid operation is provided, return an error message.
"""

def tuple_operations(t1, t2, ops):
    t1 = set(t1)
    t2 = set(t2)
    res = []

    for op in ops:
        if op == "union":
            res.append(sorted(t1.union(t2)))
        elif op == "intersection":
            res.append(sorted(t1.intersection(t2)))
        elif op == "difference":
            if t1.issubset(t2):
                return "Error: first set is a subset of the second set."
            else:
                res.append(sorted(t1.difference(t2)))
        elif op == "symmetric_difference":
            res.append(sorted(t1.symmetric_difference(t2)))
        else:
            return "Error: Invalid operation."
    
    return res