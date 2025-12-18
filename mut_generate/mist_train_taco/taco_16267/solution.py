"""
QUESTION:
Given a rod of length N inches and an array of prices, price[]. price[i] denotes the value of a piece of length i. Determine the maximum value obtainable by cutting up the rod and selling the pieces.
Note: Consider 1-based indexing.
Example 1:
Input:
N = 8
Price[] = {1, 5, 8, 9, 10, 17, 17, 20}
Output:
22
Explanation:
The maximum obtainable value is 22 by 
cutting in two pieces of lengths 2 and 
6, i.e., 5+17=22.
Example 2:
Input:
N=8
Price[] = {3, 5, 8, 9, 10, 17, 17, 20}
Output: 
24
Explanation: 
The maximum obtainable value is 
24 by cutting the rod into 8 pieces 
of length 3, i.e, 8*3=24. 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function cutRod() which takes the array A[] and its size N as inputs and returns the maximum price obtainable.
Expected Time Complexity: O(N^{2})
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 1000
1 ≤ Ai ≤ 10^{5}
"""

def cut_rod(price, n):
    N = n
    cur = [0] * (N + 1)
    
    # Initialize the current array with the base case
    for i in range(N + 1):
        cur[i] = i * price[0]
    
    # Fill the current array using the dynamic programming approach
    for ind in range(1, N):
        for length in range(N + 1):
            notTaken = cur[length]
            taken = float('-inf')
            rodLength = ind + 1
            if rodLength <= length:
                taken = price[ind] + cur[length - rodLength]
            cur[length] = max(notTaken, taken)
    
    return cur[N]