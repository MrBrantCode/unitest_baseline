"""
QUESTION:
Compute the intersection of two sets A and B without using any built-in functions or libraries for set operations. The function should be named `set_intersection`. The input sets can contain duplicate elements and may not be sorted. The solution should have a time complexity of O(n+m), where n and m are the lengths of sets A and B respectively, and use constant extra space, excluding the space required for the output. The solution should also handle the case where the input sets are extremely large and cannot fit into memory.
"""

def set_intersection(A, B):
    frequency = {}
    intersection = []
    
    for a in A:
        if a not in frequency:
            frequency[a] = 1
        else:
            frequency[a] += 1

    for b in B:
        if b in frequency and frequency[b] > 0:
            intersection.append(b)
            frequency[b] -= 1

    return intersection