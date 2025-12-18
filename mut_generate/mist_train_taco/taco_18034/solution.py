"""
QUESTION:
Given a number N. Print the minimum positive integer by which it should be divided so that the result is an odd number.
Example 1:
Input:
N = 36
Output:
4
Explanation:
36 must be divided by 4 or 12 to make it
odd. We take minimum of 4 and 12 i.e. 4.
Example 2:
Input:
N = 5
Output:
1
Explanation:
5 is already odd.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function makeNumberOdd() which takes an integer N as an input parameter and return the minimum positive integer by which it should be divided so that the result is an odd number.
Expected Time Complexity: O(LogN)
Expected Auxiliary Space: O(1)
Constraints:
1 <= N <= 100000
"""

def makeNumberOdd(N: int) -> int:
    k = 0
    for i in range(1, N + 1):
        if N % i == 0 and (N // i) % 2 == 1:
            return i