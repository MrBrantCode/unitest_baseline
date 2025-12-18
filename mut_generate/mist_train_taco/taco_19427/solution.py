"""
QUESTION:
Given an array arr[ ] of size n such that elements of arr[ ] in range [0, 1, ..n-1]. Our task is to divide the array into the maximum number of partitions that can be sorted individually, then concatenated to make the whole array sorted. 
Example 1:
Ã¢â¬â¹Input : arr[ ] = {2, 1, 0, 3}
Output : 2
Explanation:
If divide arr[] into two partitions 
{2, 1, 0} and {3}, sort then and concatenate 
then, we get the whole array sorted.
Ã¢â¬â¹Example 2:
Input : arr[ ] = {2, 1, 0, 3, 4, 5} 
Output :  4 
 
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function maxPartitions() that takes an array (arr), sizeOfArray (n), and return the maximum number of partitions. The driver code takes care of the printing.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 10^{5}
"""

def max_partitions(arr, n):
    a = arr[0]
    c = 0
    for i in range(n):
        if a < arr[i]:
            a = arr[i]
        if a == i:
            c += 1
    return c