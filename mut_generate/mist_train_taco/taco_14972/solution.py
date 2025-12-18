"""
QUESTION:
Given an array of integers arr[] and a query integer q. Find the number X from the array such that it can be converted from q to X such that F(q, X) is minimum.
F(A, B) = Number of bits flipped to change the number A to B.
If there are more than one values in arr[] such that F(q, X) is minimum print the smallest value of X for which F(q, X) is minimum.
Example 1:
Input:
n = 9, q = 1
arr[] = {5, 32, 1, 7, 10, 50, 19, 21, 2}
Output: 1
Explanation: F(1, 1) = 0, so this is the 
minimum X.
Example 2:
Input:
n = 6, q = 8
arr[] = {5, 32, 10, 7, 10, 50, 19, 21, 2}
Output: 10
Your Task:
You don't need to read input or print anything. Your task is to complete the function findX() which takes the array of integers arr, n and q as parameters and returns an integer denoting the answer.
Expected Time Complexity: O(n*logn)
Expected Auxiliary Space: O(1)
Constraints:
1 <= n <= 10^{5}
1 <= q <= 10^{6}
1 <= arr[i] <= 10^{6}
"""

def count_bit_flips(a, b):
    """Helper function to count the number of bits flipped to change a to b."""
    ans = 0
    for i in range(18):
        if a & (1 << i) != b & (1 << i):
            ans += 1
    return ans

def find_minimum_bit_flips(arr, q):
    """
    Function to find the number X from the array such that the number of bits flipped to change q to X is minimum.
    If there are multiple such numbers, return the smallest one.
    
    Parameters:
    arr (list): A list of integers.
    q (int): The query integer.
    
    Returns:
    int: The number X from the array with the minimum bit flips.
    """
    ans = -1
    cnt = float('inf')
    
    for num in arr:
        k = count_bit_flips(num, q)
        if ans == -1 or cnt > k or (cnt == k and ans > num):
            ans = num
            cnt = k
    
    return ans