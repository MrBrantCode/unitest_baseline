"""
QUESTION:
Union of two arrays can be defined as the common and distinct elements in the two arrays.
Given two sorted arrays of size n and m respectively, find their union.
Example 1:
Input: 
n = 5, arr1[] = {1, 2, 3, 4, 5}  
m = 3, arr2 [] = {1, 2, 3}
Output: 1 2 3 4 5
Explanation: Distinct elements including 
both the arrays are: 1 2 3 4 5.
 
Example 2:
Input: 
n = 5, arr1[] = {2, 2, 3, 4, 5}  
m = 5, arr2[] = {1, 1, 2, 3, 4}
Output: 1 2 3 4 5
Explanation: Distinct elements including 
both the arrays are: 1 2 3 4 5.
 
Example 3:
Input:
n = 5, arr1[] = {1, 1, 1, 1, 1}
m = 5, arr2[] = {2, 2, 2, 2, 2}
Output: 1 2
Explanation: Distinct elements including 
both the arrays are: 1 2.
Your Task: 
You do not need to read input or print anything. Complete the function findUnion() that takes two arrays arr1[], arr2[], and their size n and m as input parameters and returns a list containing the union of the two arrays. 
 
Expected Time Complexity: O(n+m).
Expected Auxiliary Space: O(n+m).
 
Constraints:
1 <= n, m <= 10^{5}
1 <= arr[i], brr[i] <= 10^{6}
"""

def find_union(arr1, arr2, n, m):
    union_li = []
    i, j = 0, 0
    
    while i < n and j < m:
        # Skip duplicates in arr1
        while i + 1 < n and arr1[i + 1] == arr1[i]:
            i += 1
        # Skip duplicates in arr2
        while j + 1 < m and arr2[j + 1] == arr2[j]:
            j += 1
        
        if arr1[i] < arr2[j]:
            union_li.append(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            union_li.append(arr2[j])
            j += 1
        else:
            union_li.append(arr2[j])
            i += 1
            j += 1
    
    # Append remaining elements from arr1
    while i < n:
        while i + 1 < n and arr1[i + 1] == arr1[i]:
            i += 1
        union_li.append(arr1[i])
        i += 1
    
    # Append remaining elements from arr2
    while j < m:
        while j + 1 < m and arr2[j + 1] == arr2[j]:
            j += 1
        union_li.append(arr2[j])
        j += 1
    
    return union_li