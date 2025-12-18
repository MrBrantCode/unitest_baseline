"""
QUESTION:
Given a number N. Find out the nearest number which is a perfect square and also the absolute difference between them.
Example 1:
Input:
N = 25
Output:
25 0
Explanation:
Since 25 is a perfect square, it is the 
closest perfect square to itself and 
absolute difference is 25-25=0.
Example 2:
Input:
N = 1500
Output:
1521 21
Explanation:
Two of the closest perfect squares to 
1521 are 1444.Thus, 1521 is the closest 
perfect square to 1500 and the absolute 
difference  between them is 1521-1500=21.
Your Task:
You don't need to read input or print anything.Your Task is to complete the function nearestPerfectSquare() which takes the number N as input parameters and returns the nearest perfect square as well as the absolute difference between them.
Expected Time Complexity:O(sqrt(N))
Expected Space Auxillary:O(1)
Constraints:
1<=N<=10^{9}
"""

import math

def nearest_perfect_square(N: int) -> tuple:
    b = int(math.sqrt(N))
    s1 = b ** 2
    s2 = (b + 1) ** 2
    d1 = abs(N - s1)
    d2 = abs(s2 - N)
    
    if d1 <= d2:
        return (s1, d1)
    return (s2, d2)