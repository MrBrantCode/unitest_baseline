"""
QUESTION:
You are given an array of size N having no duplicate elements. The array can be categorized into the following:
1.  Ascending
2.  Descending
3.  Descending Rotated
4.  Ascending Rotated
Your task is to return which type of array it is and the maximum element of that array.
 
Example 1:
Input :
N = 5 
A[] = { 2, 1, 5, 4, 3}
Output :
5 3
Explanation:
Descending rotated with maximum
element 5 
Example 2:
Input :
N = 5
A[] = { 3, 4, 5, 1, 2}
Output : 
5 4
Explanation:
Ascending rotated with maximum element 5 
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function maxNtype() which takes the array A[] and its size N as inputs and returns the largest element in the array and and integer x denoting the type of the array.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
3 <= N <= 10^{5}
1 <= A[] <= 10^{12}
"""

def determine_array_type_and_max(arr, n):
    f = arr[0]
    l = arr[-1]
    type = 1
    
    if arr == sorted(arr):
        type = 1  # Ascending
    elif arr == sorted(arr, reverse=True):
        type = 2  # Descending
    elif l > f:
        type = 3  # Descending Rotated
    elif l < f:
        type = 4  # Ascending Rotated
    
    max_element = max(arr)
    return max_element, type