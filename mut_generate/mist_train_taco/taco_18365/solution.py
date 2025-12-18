"""
QUESTION:
Given a positive integer N, check if it is a perfect square or not.
Note: Try to solve the question using only addition and subtraction operation.
 
Example 1:
Input:
N = 35
Output:
0
Explanation:
35 is not a perfect 
square.
 
Example 2:
Input:
N = 49
Output:
1
Explanation:
49 is a perfect
square.
 
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function checkPerfectSquare() which takes an integer N and returns 1 if it is a perfect square, else 0.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
Constraints:
1<= N <=10^{5}
"""

def is_perfect_square(N: int) -> int:
    k = N ** 0.5
    if int(k) * int(k) == N:
        return 1
    return 0