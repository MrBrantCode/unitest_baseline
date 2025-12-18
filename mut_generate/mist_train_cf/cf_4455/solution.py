"""
QUESTION:
Create a function named `find_unique_pairs` that takes a list of elements as input and returns a list of all unique pairs of elements in ascending order. The function should have a time complexity of O(n^2), where n is the length of the input list, and should handle negative numbers, duplicate elements, and lists with lengths up to 10^7 efficiently. It should also work correctly for unsorted lists, lists with floating-point numbers, strings, or other non-numeric elements, and should not rely on built-in functions or libraries that directly solve the problem.
"""

def find_unique_pairs(lst):
    pairs = []
    n = len(lst)
    
    for i in range(n):
        for j in range(i+1, n):
            if lst[i] != lst[j]:
                pair = (lst[i], lst[j])
                pairs.append(pair)
    
    return pairs