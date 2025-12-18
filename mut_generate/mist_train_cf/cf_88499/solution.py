"""
QUESTION:
Create a function `find_elements` that takes a list `lst` of integers and an integer `k` as input. The function should return a tuple containing the count of elements in the list that are greater than `k` and divisible by 3, along with a list of indices of these elements in the original list. The input list will contain at most 10^6 elements.
"""

def find_elements(lst, k):
    count = 0
    indices = []
    for i in range(len(lst)):
        if lst[i] > k and lst[i] % 3 == 0:
            count += 1
            indices.append(i)
    return count, indices