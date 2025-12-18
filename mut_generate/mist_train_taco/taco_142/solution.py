"""
QUESTION:
Given an array of integers arr[0..n-1], count all pairs (arr[i], arr[j]) in it such that i*arr[i] > j*arr[j],
and 0 ≤ i < j < n.
 
Example 1:
Input :
arr[] = {5, 0, 10, 2, 4, 1, 6}
Output :
5
Explanation :
Pairs which hold condition i*arr[i] > j*arr[j] are
(10, 2) (10, 4) (10, 1) (2, 1) (4, 1)
 
Example 2:
Input :
arr[] = {8, 4, 2, 1}
Output :
2
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function countPairs() which takes the array A[] and its size N as inputs and returns the required result.
 
Expected Time Complexity: O(N. log(N))
Expected Auxiliary Space: O(N. log(N))
 
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ A[ ] ≤ 10^{3}
"""

def count_pairs(arr, n):
    # Modify the array to store i * arr[i]
    for i in range(n):
        arr[i] = i * arr[i]
    
    # Temporary array for merge sort
    temp = [0] * n
    
    # Call the merge sort function to count the pairs
    return _mergeSort(arr, temp, 0, n - 1)

def merge(arr, temp, left, mid, right):
    inv_count = 0
    i = left
    j = mid
    k = left
    while i <= mid - 1 and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
            k += 1
        else:
            temp[k] = arr[j]
            k += 1
            j += 1
            inv_count = inv_count + (mid - i)
    while i <= mid - 1:
        temp[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1
    for i in range(left, right + 1):
        arr[i] = temp[i]
    return inv_count

def _mergeSort(arr, temp, left, right):
    inv_count = 0
    if right > left:
        mid = (right + left) // 2
        inv_count = _mergeSort(arr, temp, left, mid)
        inv_count += _mergeSort(arr, temp, mid + 1, right)
        inv_count += merge(arr, temp, left, mid + 1, right)
    return inv_count