"""
QUESTION:
Given K sorted lists of integers, KSortedArray[] of size N each. The task is to find the smallest range that includes at least one element from each of the K lists. If more than one such range's are found, return the first such range found.
Example 1:
Input:
N = 5, K = 3
KSortedArray[][] = {{1 3 5 7 9},
                    {0 2 4 6 8},
                    {2 3 5 7 11}}
Output: 1 2
Explanation: K = 3
A:[1 3 5 7 9]
B:[0 2 4 6 8]
C:[2 3 5 7 11]
Smallest range is formed by number 1
present in first list and 2 is present
in both 2nd and 3rd list.
Example 2:
Input:
N = 4, K = 3
KSortedArray[][] = {{1 2 3 4},
                    {5 6 7 8},
                    {9 10 11 12}}
Output: 4 9
Your Task : 
Complete the function findSmallestRange() that receives array , array size n and k as parameters and returns the output range (as a pair in cpp and array of size 2 in java and python)
Expected Time Complexity : O(n * k *log k)
Expected Auxilliary Space  : O(k)
Constraints:
1 <= K,N <= 500
0 <= a[ i ] <= 10^{5}
"""

from heapq import *

def find_smallest_range(KSortedArray, n, k):
    a = KSortedArray
    dibba = []
    start, end = 0, 0
    mini = float('inf')
    maxi = float('-inf')
    
    for i in range(k):
        mini = min(a[i][0], mini)
        maxi = max(a[i][0], maxi)
        heappush(dibba, (a[i][0], i, 0))
    
    start, end = mini, maxi
    
    while len(dibba) >= k:
        top = heappop(dibba)
        mini = top[0]
        if maxi - mini < end - start:
            start = mini
            end = maxi
        if top[2] + 1 < n:
            heappush(dibba, (a[top[1]][top[2] + 1], top[1], top[2] + 1))
            maxi = max(maxi, a[top[1]][top[2] + 1])
    
    return [start, end]