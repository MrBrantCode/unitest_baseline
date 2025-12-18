"""
QUESTION:
Find the index of the kth largest element in a list. Create a function named `find_kth_largest` that takes two parameters: a list of integers and an integer k representing the kth largest element. The function should return the index of the kth largest element in the original list. Assume k is valid and within the bounds of the list.
"""

def find_kth_largest(lst, k):
    sorted_list = sorted(lst, reverse=True)
    kth_largest = sorted_list[k-1]
    return lst.index(kth_largest)