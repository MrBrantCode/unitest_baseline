"""
QUESTION:
Given a set, we need to find the maximum and minimum possible product among all subsets of the set.
Example 1:
Input : 
arr[] = {1, 2, 3};
Output : 
Maximum product = 6
Minimum product = 1
Explanation :
Maximum product is obtained by multiplying
2, 3
Minimum product is obtained by multiplying
1
 
Example 2:
Input :
arr[] = {4, -2, 5};
Output : 
Maximum product = 20
Minimum product = -40
Explanation :
Maximum product is obtained by multiplying
4 5
Minimum product is obtained by multiplying
4, -2, 5
 
Example 3:
Input :
arr[] = {-4, -2, 3, 7, 5, 0, 1};
Output : 
Maximum product = 840
Minimum product = -420
Explanation :
Maximum product is obtained by multiplying
-4, -2, 3, 7, 5
Minimum product is obtained by multiplying
-4, 3, 7
Your Task:  
You don't need to read input or print anything. Your task is to complete the function getMaxandMinProduct() which takes the array arr[] and its size N as inputs and returns the maximum product and minimum subset product in an vector/array/list of size 2.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 20
-9 ≤ A[i] ≤ 9
"""

def getMaxandMinProduct(arr, n):
    arr.sort()
    
    if n == 1:
        return (arr[0], arr[0])
    
    if n == 2 and arr[0] < 0 and arr[1] == 0:
        return (arr[0], arr[1])
    
    k = 1
    lis = []
    maxa = 0
    
    for i in range(n):
        if arr[i] != 0:
            k *= arr[i]
        if arr[i] < 0:
            lis.append(arr[i])
    
    if len(lis) == 0:
        maxa = k
        mini = min(arr)
    elif len(lis) % 2 == 0:
        maxa = k
        mini = k // max(lis)
    elif len(lis) % 2 != 0:
        maxa = k // max(lis)
        mini = k
    
    return (mini, maxa)