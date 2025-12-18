"""
QUESTION:
You are given an array, arr of length N, and also a single integer K . Your task is to split the array arr into K non-overlapping, non-empty subarrays. For each of the subarrays, you calculate the sum of the elements in it. Let us denote these sums as S_{1},_{ }S_{2}, S_{3}, ..., S_{K}. Where S_{i }denotes the sum of the elements in the i^{th }subarray from left.
Let G = GCD( S_{1},_{ }S_{2 },S_{3 }, ...,_{ }S_{K}).
Find the maximum value of G that can be obtained. 
The array may contain duplicate elements.
Example 1:
Input:
N = 5
K = 4
arr[] = {6, 7, 5, 27, 3}
Output: 3
Explanation: 
Since K = 4, you have to split the array into 4 subarrays.
For optimal splitting, split the array into
4 subarrays as follows: [[6], [7, 5], [27], [3]]
Therefore, S_{1} = 6, S_{2} = 7 + 5 = 12, S_{3} = 27, S_{4} = 3
Hence, G = GCD(S_{1}, S_{2}, S_{3}, S_{4}) = GCD(6, 12, 27, 3) = 3
It can be shown that 3 is the maximum value of G that can be obtained.
Thus, the answer is 3.
Example 2:
Input:
N = 3
K = 2
arr[] = {1, 4, 5}
Output: 5
Explanation: 
Since K = 2, you have to split the array into 2 subarrays.
For optimal splitting, split the array into
2 subarrays as follows: [[1, 4], [5]]
Therefore, S_{1} = 1 + 4 = 5, S_{2} = 5
Hence, G = GCD(S_{1}, S_{2}) = GCD(5,5) = 5
It can be shown that 5 is the maximum value of G that can be obtained.
Thus, the answer is 5.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function solve() which takes the array arr[] and its size N and an integer K as input parameters and returns the required maximum GCD value.
 
Expected Time Complexity: O(N * x)
Expected Auxiliary Space: O(x), x is the number of factors of the sum of all elements.
Constraints:
1 <= N <= 10^{4}
1 <= K <= N
1 <= arr[i] <= 10^{5}
"""

from typing import List
import math

def max_gcd_of_subarray_sums(arr: List[int], K: int) -> int:
    N = len(arr)
    total_sum = sum(arr)
    divisors = []
    
    # Find all divisors of the total sum
    m = int(total_sum ** 0.5)
    for i in range(1, m + 1):
        if total_sum % i == 0:
            divisors.append(i)
            if i != total_sum // i:
                divisors.append(total_sum // i)
    
    # Sort divisors in descending order
    divisors.sort(reverse=True)
    
    # Prefix sum array
    prefix_sum = arr[:]
    for i in range(1, N):
        prefix_sum[i] += prefix_sum[i - 1]
    
    # Find the maximum GCD
    for x in divisors:
        count = 0
        for y in prefix_sum:
            if y % x == 0:
                count += 1
        if count >= K:
            return x
    
    return 1  # Default return value if no valid GCD is found