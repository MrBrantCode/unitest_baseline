"""
QUESTION:
Given a function `countTriplets(arr)`, where `arr` is an array of integers with length between 1 and 300 (inclusive), and each element in `arr` is between 1 and 10^8 (inclusive), calculate the count of triplets (i, j, k) where i < j <= k < n, and the cumulative XOR values of the subarray from index i to j-1 and the subarray from index j to k are equal. Return the count of such triplets.
"""

def countTriplets(arr):
    n = len(arr)
    prefix_xor = [0] * (n + 1)
    ans, count, total = 0, {}, {}
    
    for i in range(n):
        prefix_xor[i+1] = prefix_xor[i] ^ arr[i]
        
    for k in range(n+1):
        if prefix_xor[k] not in count:
            count[prefix_xor[k]] = 0
            total[prefix_xor[k]] = 0
        ans += count[prefix_xor[k]] * k - total[prefix_xor[k]]
        count[prefix_xor[k]] += 1
        total[prefix_xor[k]] += k         
    return ans