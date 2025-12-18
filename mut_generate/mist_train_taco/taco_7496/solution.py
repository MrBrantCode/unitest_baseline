"""
QUESTION:
Given two floating point numbers a and b, find a%b.
 
Example 1:
Input:
a = 36.5, b = 5.0
Output:
1.5
Explanation:
36.5 % 5.0 = 1.5
Example 2:
Input:
a = 9.7, b = 2.3
Output:
0.5
Explanation:
9.7 % 2.3 = 0.5
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function floatMod() which takes 2 doubles a, and b as input and returns a%b.
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= a,b<= 10^{3}
"""

def float_mod(a: float, b: float) -> float:
    output = round(a % b, 6)
    return output if output != int(output) else int(output)