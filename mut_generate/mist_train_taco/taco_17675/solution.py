"""
QUESTION:
Given an array of elements. The task is to calculate the cumulative frequency of each element of the array.
Note :- Cumulative frequency should be taken according to the sorted order of elements.
Example 1:
Input : Arr[] = {1, 2, 2, 1, 3, 4}
Output : 2 4 5 6
Explanation:
Here we have an array arr[] = [1, 3, 2, 
                               1, 2, 4]
Output :1->2
        2->4
        3->5
        4->6
So, the return array will have [2, 4, 5, 6] 
as an output.
Example 2:
Input : Arr[] = {1, 2, 1, 2, 1, 2}
Output : 3 6
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function countfreq() that takes an array (arr), sizeOfArray (n) and return the array of cumulative frequency values. The driver code takes care of the printing.
Expected Time Complexity: O(NLOG(N)).
Expected Auxiliary Space: O(1).
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ A[i] ≤ 10^{5}
"""

def calculate_cumulative_frequency(arr, n=None):
    if n is None:
        n = len(arr)
    
    if n == 0:
        return []
    
    arr.sort()
    cumulative_freq = []
    count = 1
    
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            cumulative_freq.append(count)
        count += 1
    
    cumulative_freq.append(count)
    return cumulative_freq