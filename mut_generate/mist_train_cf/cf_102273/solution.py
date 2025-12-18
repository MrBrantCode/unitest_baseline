"""
QUESTION:
Create a function named `find_elements` that takes a list of integers and an integer `k` as input, and returns a tuple containing the count of elements in the list that are larger than `k` and divisible by 3, along with a list of their indices. The input list is guaranteed to have no more than 10^6 elements.
"""

def find_elements(lst, k):
    count = 0
    indices = []
    for i in range(len(lst)):
        if lst[i] > k and lst[i] % 3 == 0:
            count += 1
            indices.append(i)
    return count, indices