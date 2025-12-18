"""
QUESTION:
Implement a function `find_pairs(Arr, Total)` that finds all pairs of elements in the array `Arr` that sum up to the target `Total`. The function should return a list of pairs and have a time complexity better than O(n^2). The array `Arr` contains integers and the target `Total` is also an integer. The array `Arr` may contain duplicate elements, and if a pair is found, it should be included in the result regardless of whether the elements are adjacent in the array or not.
"""

def find_pairs(Arr, Total):
    num_set = set()
    pairs = set()
    for num in Arr:
        difference = Total - num
        if difference in num_set:
            pairs.add((min(num, difference), max(num, difference)))
        num_set.add(num)
    return list(pairs)