"""
QUESTION:
Given an unsorted array of size N. Find the first element in array such that all of its left elements are smaller and all right elements to it are greater than it.
Note: Left and right side elements can be equal to required element. And extreme elements cannot be required element.
 
Example 1:
Input:
N = 4
A[] = {4, 2, 5, 7}
Output:
5
Explanation:
Elements on left of 5 are smaller than 5
and on right of it are greater than 5.
 
Example 2:
Input:
N = 3
A[] = {11, 9, 12}
Output:
-1
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function findElement() which takes the array A[] and its size N as inputs and returns the required element. If no such element present in array then return -1.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
 
Constraints:
3 <= N <= 10^{6}
1 <= A[i] <= 10^{6}
"""

def find_element(arr, n):
    if n < 3:
        return -1
    
    ans = -1
    maxi = arr[0]
    h = set()
    
    for i in range(1, n - 1):
        if arr[i] >= maxi:
            h.add(i)
            maxi = arr[i]
    
    mini = arr[-1]
    for i in range(n - 2, 0, -1):
        if i in h and arr[i] <= mini:
            ans = i
            mini = arr[i]
        if arr[i] < mini:
            mini = arr[i]
    
    if ans == -1:
        return -1
    
    return arr[ans]