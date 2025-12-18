"""
QUESTION:
A Carol number is an integer of the form 4^{n} – 2^{(n+1)} – 1. Given a number N, the task is to find the N’th Carol Number. First few carol numbers are -1, 7, 47, 223, 959… etc. 
 
Example 1:
Input:
N = 2
Output:
7
Explanation:
2^{nd} Carol Number is 7
Example 2:
Input:
N = 4
Output:
223
Explanation:
4^{th }Carol Number is 223
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function nthCarol() which takes an Integer N as input and returns the answer.
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <=^{ }15
"""

def nth_carol(N: int) -> int:
    return int(4 ** N - 2 ** (N + 1) - 1)