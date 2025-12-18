"""
QUESTION:
Given an array of digits (values are from 0 to 9), find the minimum possible sum of two numbers formed from digits of the array. All digits of the given array must be used to form the two numbers.
Any combination of digits may be used to form the two numbers to be summed.  Leading zeroes are permitted.
If forming two numbers is impossible (i.e. when n==0) then the "sum" is the value of the only number that can be formed.
 
 
Example 1:
Input:
N = 6
arr[] = {6, 8, 4, 5, 2, 3}
Output:
604
Explanation:
The minimum sum is formed by numbers 
358 and 246
 
Example 2:
Input:
N = 5
arr[] = {5, 3, 0, 7, 4}
Output:
82
Explanation:
The minimum sum is formed by numbers 
35 and 047
Your Task:
You don't have to print anything, printing is done by the driver code itself. Your task is to complete the function minSum() which takes the array A[] and its size N as inputs and returns the required sum.
Expected Time Complexity: O(N. log(N))
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 35
0 ≤ A[] ≤ 9
"""

import heapq as h

def min_sum_of_two_numbers(arr, n):
    if n == 0:
        return 0
    
    num1 = '0'
    num2 = '0'
    heap = []
    
    for i in range(n):
        h.heappush(heap, arr[i])
    
    while heap:
        if heap:
            num1 += str(h.heappop(heap))
        if heap:
            num2 += str(h.heappop(heap))
    
    return int(num1) + int(num2)