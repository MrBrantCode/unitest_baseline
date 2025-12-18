"""
QUESTION:
Create a function `generate_subsets(elements)` that generates all non-empty subsets of a given set of elements in lexicographical order. The function should not use recursion, built-in subset generation functions, or extra space proportional to the input size. It should handle duplicate elements efficiently, have a time complexity of O(2^n), and be able to handle large input sets.
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