"""
QUESTION:
Write a function `countPairsWithKXor(arr, n, k)` that calculates the number of pairs having an XOR value with precisely k set bits, where the pairs can be formed using the array elements and the numbers already included in the frequency map. The function should have a space complexity of O(n) where n is the number of elements in the array.
"""

def countPairsWithKXor(arr, n, k):
    freq = {}
    ans = 0
    
    for i in range(n):
        # Count set bits in arr[i] XOR k
        count = 0
        num = arr[i] ^ k
        while num > 0:
            count += num & 1
            num >>= 1
        
        # Add count of pairs with arr[i] and numbers already included in freq
        if count in freq:
            ans += freq[count]
        
        # Add arr[i] to freq
        if arr[i] not in freq:
            freq[arr[i]] = 0
        freq[arr[i]] += 1
    
    return ans