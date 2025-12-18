"""
QUESTION:
You are given an equation of the form x_{1}+x_{2}+...+x_{N}=K. You need to find the total number of positive integral solutions of this equation.
 
Example 1:
Input: s = a+b=5
Output: 4
Explanation: (4,1) , (1,4) , (2,3) , (3,2)
Example 2:
Input: s = a+b=1
Output: 0
Explanation: No solution exist.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function posIntSol() which takes a string as input and returns number of solutions.
Note: Distance has to be calculated with a precision of 0.0000000000001
Expected Time Complexity : O(Length of given string)
Expected Auxiliary Space : O(1)
 
Constraints:
1 <= K <= 25
2 <= N <= 10
"""

def count_positive_integral_solutions(equation: str) -> int:
    i = 0
    pcnt = 0
    
    # Count the number of '+' signs to determine the number of variables (N)
    while equation[i] != '=':
        if equation[i] == '+':
            pcnt += 1
        i += 1
    
    # Number of variables (N) is the number of '+' signs plus one
    r = pcnt + 1
    
    # Extract the value of K from the equation
    n = ''
    i += 1
    while i < len(equation):
        n += equation[i]
        i += 1
    n = int(n)
    
    # Calculate the number of positive integral solutions
    n = n - r
    if n <= 0:
        return 0
    
    # Calculate the binomial coefficient (n + r - 1) choose (r - 1)
    cnt = 0
    num = 1
    den = 1
    while cnt < n:
        num = num * (n + r - 1 - cnt)
        den = den * (cnt + 1)
        cnt += 1
    
    return num // den