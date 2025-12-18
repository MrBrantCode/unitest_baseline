"""
QUESTION:
Given a array a[] of non-negative integers. Count the number of pairs (i, j) in the array such that a[i] + a[j] < a[i]*a[j]. (the pair (i, j) and (j, i) are considered same and i should not be equal to j)
Example 1:
Input:
N=3
arr[] = {3, 4, 5} 
Output: 3
Explanation: Pairs are (3, 4) , (4, 5) and (3,5).  
 
Example 2:
Input:
N=3
arr[] = {1, 1, 1 } 
Output: 0
Your Task:
Since, this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function CountPairs() that takes array arr and integer n as parameters and return the total number of pairs possible.
 
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
 
Constraints:
1 ≤ N ≤ 10^{5}
"""

def count_pairs_satisfying_condition(arr, n):
    # Sort the array to handle the pairs more efficiently
    work = sorted(arr)
    
    # If there are 1s or 0s in the array, we can reduce the array size
    if 1 in work:
        work = work[n - work[::-1].index(1):]
    elif 0 in work:
        work = work[n - work[::-1].index(0):]
    
    # Count the number of 2s in the array
    z = work.count(2)
    
    # Calculate the total number of pairs
    v = len(work)
    x = v * (v - 1) // 2 - z * (z - 1) // 2
    
    return x