"""
QUESTION:
How many non-attacking knights K(n) can be placed on an n x n chessboard. 
Recall that a knight can attack another knight if their vertical distance on the chessboard is 2 and their horizontal distance is 1, or if their vertical distance is 1 and their horizontal distance is 2. Only one knight may be placed on each square of the chessboard.
 
Example 1:
Input:
n = 3
Output:
5
Explanation:
We can place 5 non-attacking knights
on a 3*3 chessboard.
Example 2:
Input:
n = 1
Output:
1
Explanation:
There is only one cell available and
we can place a knight on it.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function saveKnights() which takes an Integer n as input and returns the maximum number of non-attacking Knights thatr can be placed on a n*n chessboard.
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= n <= 10^{8}
"""

import math

def max_non_attacking_knights(n: int) -> int:
    if n == 2:
        return 4
    elif n % 2 == 0:
        return int(math.pow(n, 2) / 2)
    else:
        return int((math.pow(n, 2) + 1) / 2)