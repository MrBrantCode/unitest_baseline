"""
QUESTION:
Given an array arr[] of size N of non negative integers. We can perform a swap operation on any two adjacent elements in the array. The task is to find the minimum number of swaps needed to sort the array in non - decreasing order. 
 
Example 1: 
Input:
N = 4
arr[] = {4, 1, 2, 3}
Output: 3
Explanation: (4,1,2,3) -> (1,4,2,3) -> 
(1,2,4,3) -> (1,2,3,4). Hence we need 
a total of 3 swaps to sort it in 
non - decreasing order.
Ã¢â¬â¹Example 2: 
Input: 
N = 4
arr[] = {4, 4, 2, 3}
Output: 4
Explanation: (4,4,2,3) -> (4,2,4,3) ->
(4,2,3,4) -> (2,4,3,4) -> (2,3,4,4,).
Hence we need a total of 4 swap to 
sort it in increasing order.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function countSwaps() which takes the array arr[] and N as inputs and returns the minimum number of swaps needed to sort the array in non - decreasing order.
Expected Time Complexity: O(NlogN)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{4}
1 ≤ arr[i] ≤ 10^{9}
"""

def count_swaps(arr, n):
    def merge(arr, mid, l, r):
        n1 = mid - l + 1
        n2 = r - mid
        left = []
        right = []
        for i in range(n1):
            left.append(arr[l + i])
        for i in range(n2):
            right.append(arr[mid + 1 + i])
        count = 0
        i = 0
        k = l
        j = 0
        while i < n1 and j < n2:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
                count += n1 - i
            k += 1
        while i < n1:
            arr[k] = left[i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = right[j]
            j += 1
            k += 1
        return count

    def merge_sort(arr, l, r):
        count = 0
        if l < r:
            mid = (l + r) // 2
            count += merge_sort(arr, l, mid)
            count += merge_sort(arr, mid + 1, r)
            count += merge(arr, mid, l, r)
        return count

    return merge_sort(arr, 0, n - 1)