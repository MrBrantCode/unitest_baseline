"""
QUESTION:
Given two coordinates (x, y) and (a, b). Find if it is possible to reach (x,y) from (a,b).
Only possible moves from any coordinate (i, j) are-
	(i-j, j)
	(i, i-j)
	(i+j, j)
	(i, i+j)
 
Example 1:
Input:
x = 1, y = 1, a = 2, b = 3
Output:
1
Explanation:
We can reach the point (2,3) from (1,1).
Example 2:
Input:
x = 35, y = 15, a = 20, b = 25
Output:
1
Explanation:
We can reach the point (20,25) from (35,15).
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function isPossible() which takes 4 Integers x, y, a and b as input and returns 1 if it's possible to move to (a,b) from (x,y) else returns 0.
 
Expected Time Complexity: O(log(x))
Expected Auxiliary Space: O(1)
 
Constraints:
-10^{5} <= x,y,a,b <= 10^{5}
"""

def is_possible_to_reach(x: int, y: int, a: int, b: int) -> int:
    def gcd(x: int, y: int) -> int:
        x = abs(x)
        y = abs(y)
        if x < y:
            (x, y) = (y, x)
        while y:
            (x, y) = (y, x % y)
        return x
    
    if gcd(x, y) == gcd(a, b):
        return 1
    else:
        return 0