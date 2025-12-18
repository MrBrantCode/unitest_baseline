"""
QUESTION:
Write a function named `countPairsWithKXor` that takes an array `arr`, its size `n`, and an integer `k` as input and returns the number of pairs that can be formed using the array elements and the numbers already included in the frequency map such that the XOR value of the pair has precisely `k` set bits. The function should have a space complexity of O(n).
"""

def countPairsWithKXor(arr, n, k):
    freq = {}
    ans = 0
    
    for i in range(n):
        count = 0
        num = arr[i] ^ k
        while num > 0:
            count += num & 1
            num >>= 1
        
        if count in freq:
            ans += freq[count]
        
        if count not in freq:
            freq[count] = 0
        freq[count] += 1
    
    return ans