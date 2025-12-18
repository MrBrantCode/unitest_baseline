"""
QUESTION:
Given two arrays a[] and b[] of same size.Your task is to find minimum sum of two elements such that they belong to different arrays and are not at same index in their arrays.
Example 1:
Input : 
a[] = {5, 4, 13, 2, 1}
b[] = {2, 3, 4, 6, 5}
Output : 
3
Explanation :
We take 1 from a[] and 2 from b[]
Sum is 1 + 2 = 3.
 
Example 2:
Input : 
a[] = {5, 4, 13, 1}
b[] = {3, 2, 6, 1}
Output : 
3
Explanation :
We take 1 from a[] and 2 from b[].
Note that we can't take 1 from b[]
as the elements can not be at same
index. 
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function minSum() which takes the array A[], B[] and its size N as inputs and returns the minimum sum.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
1<=N<=10^{5}
1<=a[i]<=10^{5}
1<=b[i]<=10^{5}
"""

def min_sum_of_different_elements(a, b, n):
    # Find the minimum elements in both arrays
    a1 = min(a)
    b1 = min(b)
    
    # Check if the indices of the minimum elements are different
    if a.index(a1) != b.index(b1):
        return a1 + b1
    else:
        # Sort the arrays to find the second smallest elements
        a.sort()
        b.sort()
        a2 = a[1]
        b2 = b[1]
        # Return the minimum of the two possible sums
        return min(a1 + b2, a2 + b1)