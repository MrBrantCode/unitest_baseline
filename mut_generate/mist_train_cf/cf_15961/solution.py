"""
QUESTION:
Write a function `generate_subsets` that generates all non-empty subsets of a given set of elements in lexicographical order. The function should not use any built-in subset generation functions, should have a time complexity of O(2^n), and should use an iterative approach. The function should also handle duplicate elements efficiently and not use extra space proportional to the size of the input set.
"""

def generate_subsets(elements):
    sorted_elements = sorted(elements)
    n = len(sorted_elements)
    subsets = []

    for i in range(1, 2**n):
        subset = []
        for j in range(n):
            if (i >> j) & 1:
                subset.append(sorted_elements[j])
        if subset:
            subsets.append(subset)

    return subsets