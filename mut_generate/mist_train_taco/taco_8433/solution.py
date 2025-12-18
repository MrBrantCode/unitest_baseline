"""
QUESTION:
Given an array arr[] of N integers, the task is to find the number of pairs in the array whose XOR is odd.
Example 1:
Input: N = 3, arr[] = {1, 2, 3}
Output: 2
Explanation: All pairs of array
             1 ^ 2 = 3
             1 ^ 3 = 2
             2 ^ 3 = 1
Example 2:
Input: N = 2, arr[] =  {1, 2}
Output: 1
Explanation: 1^2 =3 which is odd.
Your Task:
This is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function countXorPair() that takes array arr and integer N as parameters and returns the desired output.
 
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
 
Constraints:
1 ≤ N ≤ 10^{6}
"""

def count_odd_xor_pairs(arr, N):
    even_count = 0
    odd_count = 0
    
    for i in range(N):
        if arr[i] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    return even_count * odd_count