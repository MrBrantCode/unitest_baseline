"""
QUESTION:
Given two values ‘a’ and ‘b’ that represent coefficients in “ax – by = 0”, find the smallest values of x and y that satisfy the equation. It may also be assumed that x > 0, y > 0, a > 0 and b > 0.
Example 1:
Input: a = 25, b = 35
Output: 7 5
Explaination: 25*7 - 35*5 = 0. And x = 7 
and y = 5 are the least possible values 
of x and y to get the equation solved.
Example 2:
Input: a = 3, b = 7
Output: 7 3
Explaination: For this case x = 7 and 
y = 3 are the least values of x and y 
to satisfy the equation.
Your Task:
You do not need to read input or print anything. Your task is to complete the function findXY() which takes a and b as input parameters and returns the least possible values of x and y to satisfy the equation.
Expected Time Complexity: O(log(max(a, b)))
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ a, b ≤ 10^{4}
"""

def find_smallest_xy(a: int, b: int) -> tuple:
    import math
    
    # Calculate the greatest common divisor (GCD) of a and b
    gcd_ab = math.gcd(a, b)
    
    # Calculate the smallest values of x and y
    x = b // gcd_ab
    y = a // gcd_ab
    
    return (x, y)