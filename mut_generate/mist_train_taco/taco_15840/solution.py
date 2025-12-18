"""
QUESTION:
Given an array of distinct integers. The task is to count all the triplets such that sum of two elements equals the third element.
 
Example 1: 
Input: 
N = 4 
arr[] = {1, 5, 3, 2}
Output: 2 
Explanation: There are 2 triplets:
 1 + 2 = 3 and 3 +2 = 5
Example 2: 
Input: 
N = 3
arr[] = {2, 3, 4}
Output: 0
Explanation: No such triplet exits
Your Task:  
You don't need to read input or print anything. Your task is to complete the function countTriplet() which takes the array arr[] and N as inputs and returns the triplet count
Expected Time Complexity: O(N^{2})
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{3}
1 ≤ arr[i] ≤ 10^{5}
"""

def count_triplets(arr, n):
    arr.sort()
    count = 0
    for i in range(n - 1, 1, -1):
        j = 0
        k = i - 1
        while j < k:
            if arr[j] + arr[k] == arr[i]:
                count += 1
                j += 1
                k -= 1
            elif arr[j] + arr[k] < arr[i]:
                j += 1
            else:
                k -= 1
    return count