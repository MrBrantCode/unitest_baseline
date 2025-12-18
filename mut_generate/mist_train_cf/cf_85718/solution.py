"""
QUESTION:
Write a function named `kConcatenationMaxSum` that takes two parameters: an integer array `arr` and an integer `k`. The function should return the minimum sub-array sum of the modified array obtained by repeating `arr` `k` times. If the sub-array sum can be `0`, the function should return `0` in that case. The answer should be returned modulo `10^9 + 7`. 

Constraints: 
`1 <= len(arr) <= 10^5`
`1 <= k <= 10^5`
`-10^4 <= arr[i] <= 10^4`
"""

def kConcatenationMaxSum(arr, k: int):
    L, res, mod = len(arr), 0, int(1e9+7)
    pre_sum = [0]*(L+1)
    suf_sum = [0]*(L+1)
    for i in range(1, L+1):
        pre_sum[i] = max(pre_sum[i-1]+arr[i-1], arr[i-1])
    for i in range(L-1, -1, -1):
        suf_sum[i] = max(suf_sum[i+1]+arr[i], arr[i])
        
    a_max = max(arr)
    if a_max < 0: return 0
    total_sum = sum(arr)
    if k == 1: return max(max(pre_sum), max(suf_sum)) % mod
    if total_sum < 0: return max(max(pre_sum), max(suf_sum)) % mod
    return max(max(pre_sum), max(suf_sum), pre_sum[-1]+suf_sum[0]+total_sum*(k-2)) % mod