"""
QUESTION:
Given an unsorted array arr[] of N integers and a sum. The task is to count the number of subarrays which add to a given number.
 
Example 1:
Input:
N=5
sum=-10
arr[] = { 10, 2, -2, -20, 10 }
Output:  3
Explanation:
Subarrays with sum -10 are: 
[10, 2, -2, -20], [2, -2, -20, 10]
and [-20, 10].
 
Example 2:
Input:
N=6
sum= 33
arr[] = { 1, 4, 20, 3, 10, 5 }
Output:  1
Your Task:
Since, this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function subArraySum() that takes array arr , integer N and integer sum as parameters and returns the count of the subarray which adds to the given sum.
 
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
 
Constraints:
1 ≤ N ≤ 10^{6}
"""

def count_subarrays_with_sum(arr, N, sum):
    currsum = {}
    currsum[0] = 1
    sums = 0
    count = 0
    for i in range(N):
        sums += arr[i]
        if sums - sum in currsum:
            count += currsum[sums - sum]
        if sums in currsum:
            currsum[sums] += 1
        else:
            currsum[sums] = 1
    return count