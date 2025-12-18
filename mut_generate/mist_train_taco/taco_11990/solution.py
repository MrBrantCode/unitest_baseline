"""
QUESTION:
Given an array arr[] of size N,the task is to arrange the array such that odd elements occupy the odd positions and even elements occupy the even positions. The order of elements must remain the same. Consider zero-based indexing. After printing according to conditions, if remaining, print the remaining elements as it is.
Example 1:
Input: N = 6
arr[] = {1, 2, 3, 4, 5, 6}
Output: 2 1 4 3 6 5
Explanation: Even elements are at 
even position and odd elements are 
at odd position keeping the order 
maintained.
Example 2:
Input: N = 4, arr[] = {3, 2, 4, 1}
Output: 2 3 4 1
 
Your Task:
This is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function arrangeOddAndEven() that takes array arr[] and size N as parameters and returns an array according to the above-mentioned condition.
 
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
 
Constraints:
2 ≤ N ≤ 10^{6}
"""

def arrange_odd_even(arr, n):
    even_elements = []
    odd_elements = []
    
    # Separate even and odd elements
    for num in arr:
        if num % 2 == 0:
            even_elements.append(num)
        else:
            odd_elements.append(num)
    
    i = 0
    j = 0
    
    # Rearrange the array
    while i < n:
        if j < len(even_elements):
            arr[i] = even_elements[j]
            i += 1
        if j < len(odd_elements):
            arr[i] = odd_elements[j]
            i += 1
        j += 1
    
    return arr