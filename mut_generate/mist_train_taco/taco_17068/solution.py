"""
QUESTION:
Given an integer N. FInd an integer K for which N%K is the largest ( 1 <= K < N).
 
Example 1:
Input:
N = 3
Output:
2
Explanation:
3%1 = 0
3%2 = 1
So, the modulo is highest for 2.
Example 2:
Input:
N = 4
Output:
3
Explanation:
4%1 = 0
4%2 = 0
4%3 = 1
So, the modulo is highest for 3.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function modTask() which takes a Integer N as input and returns an integer K(1 <= K < N) for which N%K is largest.
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{18}
"""

def find_max_modulo_k(N: int) -> int:
    if N % 2 == 1:
        return (N + 1) // 2
    else:
        return N // 2 + 1