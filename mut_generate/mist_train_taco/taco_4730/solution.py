"""
QUESTION:
Check Tutorial tab to know how to to solve.  

Task 

The provided code stub reads two integers from STDIN, $\boldsymbol{\alpha}$ and $\boldsymbol{b}$.  Add code to print three lines where: 

 The first line contains the sum of the two numbers.   
 The second line contains the difference of the two numbers (first - second).   
 The third line contains the product of the two numbers.   

Example 

$\boldsymbol{a}=3$ 

$b=5$  

Print the following:

8
-2
15

Input Format

The first line contains the first integer, $\boldsymbol{\alpha}$. 

The second line contains the second integer, $\boldsymbol{b}$.  

Constraints

$1\leq a\leq10^{10}$ 

$1\leq b\leq10^{10}$  

Output Format

Print the three lines as explained above.   

Sample Input 0
3
2

Sample Output 0
5
1
6

Explanation 0

$3+2\implies5$ 

$3-2\Longrightarrow1$ 

$3*2\Longrightarrow6$
"""

def perform_arithmetic_operations(a: int, b: int) -> tuple:
    """
    Performs arithmetic operations on two integers and returns the results.

    Parameters:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    tuple: A tuple containing three integers:
           - The sum of a and b.
           - The difference when a is subtracted from b.
           - The product of a and b.
    """
    add = a + b
    sub = a - b
    mul = a * b
    return (add, sub, mul)