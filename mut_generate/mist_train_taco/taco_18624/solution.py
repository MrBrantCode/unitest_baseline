"""
QUESTION:
Given an integer N, check if it is possible to represent it as a function(a, b) such that : a^{2} + b^{2} = N where "a" and "b" are whole numbers. Print 1 if it's possible, else Print 0.
 
Example 1:
Input:
N = 1
Output:
1
Explanation:
1^{2} + 0^{2} = 1. So, the Output is 1
Example 2:
Input:
N = 2
Output:
1
Explanation:
1^{2} + 1^{2} = 2. So, the Output is 1
Example 3:
Input:
N = 7
Output:
0
Explanation:
We don't have a or b, which when summed
after squaring gives 7. So, Output is 0.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function checkSquares() which takes an Integer N as input and returns the answer.
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{6}
"""

import math

def can_be_sum_of_squares(N: int) -> int:
    for a in range(int(math.sqrt(N)) + 1):
        for b in range(int(math.sqrt(N)) + 1):
            if a * a + b * b == N:
                return 1
    return 0