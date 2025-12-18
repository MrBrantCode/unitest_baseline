"""
QUESTION:
Find the longest increasing subsequence of consecutive integers in a given series of integers. The subsequence does not have to be contiguous in the original series, but it must be strictly increasing and composed of consecutive integers. Write a function `longest_increasing_subseq(nums)` that takes a list of integers `nums` as input and returns the longest increasing subsequence of consecutive integers.
"""

def longest_increasing_subseq(nums):
    if not nums: return []
    
    n = len(nums)
    tails, lengths = [0]*n, [1]*n
    
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                if lengths[j] + 1 > lengths[i]:
                    lengths[i] = lengths[j] + 1
                    tails[i] = j

    # Reconstruct the longest increasing subsequence
    idx = lengths.index(max(lengths))
    lis = []
    while len(lis) < max(lengths):
        lis.append(nums[idx])
        idx = tails[idx]
        
    return lis[::-1]