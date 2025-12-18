"""
QUESTION:
Given an integer array A and an integer K, write a function `subarraysDivByK` that determines the count of contiguous, non-empty subarrays whose sum is divisible by K. The function should take in two parameters, A and K, and return the count of such subarrays. The constraints are 1 <= len(A) <= 30000, -10000 <= A[i] <= 10000, and 2 <= K <= 10000.
"""

def subarraysDivByK(A, K):
    prefix_sums = {0: 1}
    curr_sum = output = 0
    for num in A:
        curr_sum += num
        modulus = curr_sum % K
        if modulus < 0:  # handle negative numbers, because -1 % 5 = -1 in Python
            modulus += K
        output += prefix_sums.get(modulus, 0)
        prefix_sums[modulus] = prefix_sums.get(modulus, 0) + 1
    return output