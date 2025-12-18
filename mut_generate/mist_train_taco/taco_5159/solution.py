"""
QUESTION:
Given a number N, find the N^{th} term in the series 1, 3, 6, 10, 15, 21…
 
Example 1:
Input :
N = 4 
Output:
10
Explanation:
The 4^{th} term of the Series is 10.
Example 2:
Input :
N = 3 
Output:
6
Explanation:
The 3^{rd} term of the Series is 6.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function findNthTerm() which takes an Integer N as input and returns the answer.
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{4}
"""

def find_nth_term(N: int) -> int:
    return int(N * (N + 1) / 2)