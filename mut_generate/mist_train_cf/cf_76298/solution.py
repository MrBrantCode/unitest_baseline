"""
QUESTION:
Write a function `countSubarrays(arr)` that takes an array of integers `arr` and returns the number of sub-arrays with an odd sum and an even product. The function should return the result modulo `10^9 + 7`. The input array `arr` has the following constraints: `1 <= arr.length <= 10^5` and `1 <= arr[i] <= 100`.
"""

def countSubarrays(arr):
    n = len(arr)
    odd = [0] * (n + 1)
    even = [0] * (n + 1)
    for i in range(n):
        if arr[i] % 2 == 0:
            even[i + 1] = even[i] + 1
            odd[i + 1] = odd[i]
        else:
            even[i + 1] = odd[i]
            odd[i + 1] = even[i] + 1
        
    return sum(even) % (10**9 + 7)