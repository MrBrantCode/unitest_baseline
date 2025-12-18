"""
QUESTION:
Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.
Example 1:
Input:
N = 4, K = 6
arr[] = {1, 5, 7, 1}
Output: 2
Explanation: 
arr[0] + arr[1] = 1 + 5 = 6 
and arr[1] + arr[3] = 5 + 1 = 6.
Example 2:
Input:
N = 4, K = 2
arr[] = {1, 1, 1, 1}
Output: 6
Explanation: 
Each 1 will produce sum 2 with any 1.
Your Task:
You don't need to read input or print anything. Your task is to complete the function getPairsCount() which takes arr[], n and k as input parameters and returns the number of pairs that have sum K.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 <= N <= 10^{5}
1 <= K <= 10^{8}
1 <= Arr[i] <= 10^{6}
"""

from collections import Counter

def count_pairs_with_sum(arr, k):
    mpp = Counter(arr)
    count = 0
    unique_elements = list(set(arr))
    
    for num in unique_elements:
        complement = k - num
        if complement in mpp:
            if complement == num:
                n = mpp[num]
                count += n * (n - 1) // 2
            else:
                count += mpp[num] * mpp[complement]
    
    return count