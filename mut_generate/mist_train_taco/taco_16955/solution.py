"""
QUESTION:
You are given an array of N integers arr, find the count of reverse pairs. 
A pair of indices (i, j) is said to be a reverse pair if both the following conditions are met:
	0 <= i < j < N 
	arr[i] > 2 * arr[j]
Example 1:
Input:
N = 6
arr = [3, 2, 4, 5, 1, 20]
Output:
3
Explanation:
The Reverse pairs are 
(i)  (0, 4), arr[0] = 3, arr[4] = 1, 3 > 2(1) 
(ii) (2, 4), arr[2] = 4, arr[4] = 1, 4 > 2(1) 
(iii)(3, 4), arr[3] = 5, arr[4] = 1, 5 > 2(1) 
 
Example 2:
Input: 
N = 5
arr= [2, 4, 3, 5, 1]
Output: 
3
Explanation: 
(i)   (1, 4), arr[1] = 4, arr[4] = 1, 4 > 2 * 1
(ii)  (2, 4), arr[2] = 3, arr[4] = 1, 3 > 2 * 1
(iii) (3, 4), arr[3] = 5, arr[4] = 1, 5 > 2 * 1
 
Your Task:
Complete the function countRevPairs(), which takes integer a list of N integers as input and returns the count of Reverse Pairs.
Expected Time Complexity: O(N logN)
Expected Auxiliary Space: O(N)
Constraints:
1 <= N <= 50000
1 <= arr[i] <= 10^{9}
"""

import bisect

def count_reverse_pairs(arr):
    temp = []
    count = 0
    for i in range(len(arr)):
        count += len(temp) - bisect.bisect_right(temp, 2 * arr[i])
        bisect.insort(temp, arr[i])
    return count