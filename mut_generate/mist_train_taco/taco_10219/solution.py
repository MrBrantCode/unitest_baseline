"""
QUESTION:
Given an array arr[] containing N integers. In one step, any element of the array can either be increased or decreased by one. Find minimum steps required such that the product of the array elements becomes 1. 
 
Example 1:
Input:
N = 3
arr[] = {-2, 4, 0}
Output:
5
Explanation:
We can change -2 to -1, 0 to -1 and 4 to 1.
So, a total of 5 steps are required
to update the elements such that
the product of the final array is 1. 
Example 2:
Input:
N = 3
arr[] = {-1, 1, -1} 
Output :
0
Explanation:
Product of the array is already 1.
So, we don't need to change anything.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function makeProductOne() which takes an integer N and an array arr of size N as input and returns the minimum steps required.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{5}
-10^{3} ≤ arr[i] ≤ 10^{3}
"""

def make_product_one(arr, N):
    p = 0
    n = 0
    z = 0
    step = 0
    
    for i in range(N):
        if arr[i] == 0:
            z += 1
        elif arr[i] < 0:
            n += 1
            step += (-1 - arr[i])
        else:
            p += 1
            step += (arr[i] - 1)
    
    if n % 2 == 0:
        step += z
    elif z > 0:
        step += z
    else:
        step += 2
    
    return step