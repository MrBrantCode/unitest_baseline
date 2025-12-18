"""
QUESTION:
Develop a function `longest_increasing_subseq` that identifies the longest continuously increasing subsequence in a given list of integers. The function should return the longest subsequence. 

The function must handle lists of any length, including empty lists. The function should be able to handle duplicate elements. The time complexity should be at most O(n^2), where n is the number of elements in the list.
"""

def longest_increasing_subseq(my_list):
    if not my_list:
        return []

    seq = [1] * len(my_list)
    prev = [None] * len(my_list)
    
    for i in range(len(my_list)):
        for j in range(i):
            if my_list[i] > my_list[j] and seq[i] < seq[j] + 1:
                seq[i] = seq[j] + 1
                prev[i] = j 

    idx = seq.index(max(seq))
    result = []

    while idx is not None:
        result.append(my_list[idx])
        idx = prev[idx]
        
    return result[::-1]