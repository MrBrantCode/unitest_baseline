"""
QUESTION:
An element Y is said to be the surpasser of element X if it is a greater element on the right of X. ie, if X = arr[i] and Y = arr[j], i<j and Arr[i] < Arr[j]. 
Given an array of size N containing distinct integers, find the number of surpassers for each of its elements.
Example 1:
Input:
N = 5
Arr[] = {4, 5, 1, 2, 3}
Output: 1 0 2 1 0
Explanation: There are no elements greater 
than 3 at the right of 3. There is one 
element at right of 2 and greater than 2. 
There are 2 elements greater than 1 at the 
right of 1. And so on.
Example 2:
Input:
N = 6
Arr[] = {2, 7, 5, 3, 8, 1}
Output: 4 1 1 1 0 0
Your Task:
You don't need to read input or print anything. Your task is to complete the function findSurpasser() which takes the array of integers arr and n as input parameters and returns an array of integers of size N denoting the surpasser count of each element of arr.
Expected Time Complexity: O(N*logN)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ Arr[i] ≤ 10^{6}
"""

def find_surpasser_counts(arr, n):
    d = {}

    def merge(l, m, r):
        L = arr[l:m + 1]
        R = arr[m + 1:r + 1]
        i = 0
        j = 0
        k = l
        c = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                d[L[i]] = d.get(L[i], 0) + c
                i += 1
                k += 1
            else:
                arr[k] = R[j]
                c += 1
                j += 1
                k += 1
        while j < len(R):
            arr[k] = R[j]
            c += 1
            j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            d[L[i]] = d.get(L[i], 0) + c
            i += 1
            k += 1

    def mergesort(i, j):
        if j - i > 0:
            m = i + (j - i) // 2
            mergesort(i, m)
            mergesort(m + 1, j)
            merge(i, m, j)
    
    ans = []
    du = arr[:]
    mergesort(0, n - 1)
    for i in du:
        ans.append(n - 1 - d.get(i, 0))
        n -= 1
    return ans