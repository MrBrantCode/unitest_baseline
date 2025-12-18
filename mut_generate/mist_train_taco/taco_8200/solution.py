"""
QUESTION:
Given an integer array arr of size N and an integer k, return the number of good subarrays of arr.
A good array is an array where the number of different integers in that is exactly k.
	For example, {1, 3, 4, 4, 1} has 3 different integers: 1, 3, and 4.
Note : A subarray is a contiguous part of an array.
Example 1:
Input:
N = 5
k = 2
arr[ ] = {1, 2, 1, 2, 3}
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: {1, 2}, {2, 1}, {1, 2}, {2, 3}, {1, 2, 1}, {2, 1, 2}, {1, 2, 1, 2}.
 
Example 2:
Input:
N = 5
k = 3
arr[ ] = {1, 2, 1, 3, 4}
Output: 3
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function subarrayCount() which takes the array of integers arr , an integer N and k as parameters and returns a number of good subarrays.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ k ≤ N
^{1 }≤ arr_{i  }≤ N
"""

def count_good_subarrays(arr, k):
    def at_most_k(arr, k):
        count = 0
        i = 0
        j = 0
        a = {}
        while j < len(arr):
            a[arr[j]] = a.get(arr[j], 0) + 1
            while len(a) > k:
                a[arr[i]] -= 1
                if a[arr[i]] == 0:
                    del a[arr[i]]
                i += 1
            count += j - i + 1
            j += 1
        return count
    
    return at_most_k(arr, k) - at_most_k(arr, k - 1)