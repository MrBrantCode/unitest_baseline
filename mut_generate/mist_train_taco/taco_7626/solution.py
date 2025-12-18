"""
QUESTION:
Given an array of N integers. Write a program to check whether an arithmetic progression can be formed using all the given elements. 
 
Example 1:
Input:
N=4
arr[] = { 0,12,4,8 }
Output: YES
Explanation: Rearrange given array as
{0, 4, 8, 12}  which forms an
arithmetic progression.
Example 2:
Input:
N=4
arr[] = {12, 40, 11, 20}
Output: NO
 
Your Task:
Since, this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function checkIsAP() that takes array arr and integer N as parameters and return true for "Yes" and false for "No".
 
Expected Time Complexity: O(NLogN).
Expected Auxiliary Space: O(1).
 
Constraints:
2 ≤ N ≤ 10^{5}
"""

def is_arithmetic_progression(arr, n):
    # Sort the array
    arr.sort()
    
    # If the array has 2 or fewer elements, it is always an AP
    if n <= 2:
        return True
    
    # Calculate the common difference
    common_diff = arr[1] - arr[0]
    
    # Check if all consecutive elements have the same difference
    for i in range(2, n):
        if arr[i] - arr[i - 1] != common_diff:
            return False
    
    return True