"""
QUESTION:
Given an array of positive integers of size N. Count the number of good pairs (i,j) such that:
	1≤ i ≤ N,
	1≤ j ≤ N
	and arr_{i} < arr_{j}.
Example 1
Input:
N = 2
arr[] = {2, 1}  
Output: 1
Explanation : The only good pair is (2,1). 
Example 2
Input:
N = 3
arr[] = {2 ,3, 2}
Output: 2
Explanation: The two good pairs are (2,3) 
and (3,2).
Your Task:
You don't need to read input or print anything. Your task is to complete the function solve() which takes the array arr[] and its size N as inputs and returns the count of good pairs as described in the problem description.
Expected Time Complexity: O(N log N)
Expected Auxiliary Space: O(1)
Constraints:
1 <= N <= 10^5
1 <= a[i] <= 10^3
"""

def count_good_pairs(arr: list, n: int) -> int:
    def binary_search(arr, key, n):
        l = 0
        r = n - 1
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] > key:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans

    arr.sort()
    count = 0
    for i in arr:
        ans = binary_search(arr, i, n)
        if ans != -1:
            count += n - ans
    return count