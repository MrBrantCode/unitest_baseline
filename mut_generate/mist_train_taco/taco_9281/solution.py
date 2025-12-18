"""
QUESTION:
Given an array Arr[] of size N. For every element in the array, the task is to find the index of the farthest element in the array to the right which is smaller than the current element. If no such number exists then print -1.
Note: 0 based indexing.
Example 1:
Input: 
N=5
Arr[] = {3, 1, 5, 2, 4}
Output: 
3 -1 4 -1 -1
Explanation:
Arr[3] is the farthest smallest element
to the right of Arr[0].
Arr[4] is the farthest smallest element
to the right of Arr[2].
And for the rest of the elements, there is
no smaller element to their right.
Example 2:
Input: 
N=5
Arr[] = {1, 2, 3, 4, 0}
Output: 
4 4 4 4 -1
Your Task: 
You don't need to read input or print anything. Your task is to complete the function farNumber() which takes the N (number of elements in Array Arr) ,Arr[], and returns the array of farthest element to the right for every element of the array.
Expected Time Complexity: O(N*logN)
Expected Auxiliary Space: O(N)
Constraints:
1  ≤  N ≤  1e5
0 ≤  Arr[i] ≤  1e9
"""

def find_farthest_smaller_right(arr):
    n = len(arr)
    l = []
    res = [-1] * n
    
    for i in range(n):
        l.append([arr[i], i])
    
    l.sort()
    mind = None
    
    for i in range(n):
        if mind is None or mind < l[i][1]:
            mind = l[i][1]
        else:
            res[l[i][1]] = mind
    
    return res