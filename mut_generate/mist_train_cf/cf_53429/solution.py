"""
QUESTION:
Write a function named `subsets` that takes an array `arr` as input and returns all possible subsets of `arr`. The function should generate subsets using bitmasking and return them in a list of lists, where each inner list is a subset of `arr`. The order of the subsets does not matter, and the function should include the empty set as one of the subsets.
"""

def subsets(arr):
    n = len(arr)
    output = []
    
    # for each mask from 0 to 2**n-1
    for bit in range(2**n):
        # create binary representation of mask
        bin_mask = bin(bit)[2:].zfill(n)
        # use binary mask to generate a subset
        output.append([arr[i] for i in range(n) if bin_mask[i]=='1'])
    return output