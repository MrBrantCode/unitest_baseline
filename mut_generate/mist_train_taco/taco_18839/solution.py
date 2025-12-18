"""
QUESTION:
Given an array A of N integers. The task is to find if there are two pairs (a, b) and (c, d) such that a+b = c+d.
Example 1:
Input:N=7 A[] = {3, 4, 7, 1, 2, 9, 8} Output: 1Explanation:(3, 7) and (9, 1) are the pairs whosesum are equal.  
Example 2:
Input:N=7 A[] = {65, 30, 7, 90, 1, 9, 8}Output: 0
 
Your Task:
Since, this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function findPairs() that takes array a and nas parametersand return 1 if pair exists else 0.
Expected Time Complexity:O(N^{2}).
Expected Auxiliary Space:O(N^{2}).
Constraints:
1 ≤ N ≤ 10^{3}
"""

def find_pairs_with_equal_sum(arr, n):
    # List to store the sums of pairs
    sums = []
    
    # Iterate through the array to find pairs and their sums
    for i in range(n):
        for j in range(i + 1, n):
            pair_sum = arr[i] + arr[j]
            # Check if this sum has been seen before
            if pair_sum in sums:
                return 1
            else:
                sums.append(pair_sum)
    
    # If no such pairs are found, return 0
    return 0