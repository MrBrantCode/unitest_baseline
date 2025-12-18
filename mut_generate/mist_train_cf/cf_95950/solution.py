"""
QUESTION:
Write a function named `find_pairs` that takes three arguments: `num`, a list of integers, and a list of target sums. The function should return all pairs of indices in the list where the sum of the corresponding elements equals one of the target sums. The pairs should be returned in ascending order of their first index. The function should have a time complexity of O(n^2 * m), where n is the length of the list and m is the length of the target sums list.
"""

def find_pairs(num, integers, target_sums):
    pairs = []
    for i in range(len(integers)):
        for j in range(i + 1, len(integers)):
            if integers[i] + integers[j] in target_sums:
                pairs.append((i, j))
    return sorted(pairs, key=lambda x: x[0])