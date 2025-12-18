"""
QUESTION:
A Diophantine equation is a polynomial equation, usually in two or more unknowns, such that only the integral solutions are required. An Integral solution is a solution such that all the unknown variables take only integer values.
Given three integers A, B, C representing a linear equation of the form: Ax + By = C. Determine if the equation has a solution such that x and y are both integral values.
 
Example 1:
Input: 
A = 3
B = 6
C = 9 
Output: 
1 
Explanation:
It is possible to
write A, B, C in the
for 3 + 6 = 9
Example 2:
Input: 
A = 4
B = 2
C = 3
Output: 
0 
Explanation:
It is not possible to
represent A, B, C in 
Diophantine equation form.
Your Task:
You don't need to read input or print anything. Your task is to complete the function isPossible() which takes three integer values A, B, C as input parameters and returns 1 if the solution for x and y exist otherwise return 0.
 
Expected Time Complexity: O(log N)
Expected Space Complexity: O(1)
 
Constraints:
1 <= A,B,C <= 10^{5}
"""

import math

def is_diophantine_solution_possible(A: int, B: int, C: int) -> int:
    k = math.gcd(A, B)
    if C % k == 0:
        return 1
    else:
        return 0