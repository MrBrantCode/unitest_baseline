"""
QUESTION:
Check the Tutorial tab to know learn about division operators.  

Task 

The provided code stub reads two integers, $\boldsymbol{\alpha}$ and $\boldsymbol{b}$, from STDIN.  

Add logic to print two lines. The first line should contain the result of integer division, $\boldsymbol{\alpha}$ // $\boldsymbol{b}$. The second line should contain the result of float division, $\boldsymbol{\alpha}$ / $\boldsymbol{b}$.  

No rounding or formatting is necessary.

Example 

$\boldsymbol{a}=3$ 

$b=5$  

The result of the integer division $3/5=0$.  
The result of the float division is $3/5=0.6$.  

Print:

0
0.6

Input Format

The first line contains the first integer, $\boldsymbol{\alpha}$. 

The second line contains the second integer, $\boldsymbol{b}$.

Output Format

Print the two lines as described above.  

Sample Input 0
4
3

Sample Output 0
1
1.33333333333

Check the Tutorial tab to know learn about division operators.  

Task 

The provided code stub reads two integers, $\boldsymbol{a}$ and $\boldsymbol{b}$, from STDIN.  

Add logic to print two lines. The first line should contain the result of integer division, $\boldsymbol{a}$ // $\boldsymbol{b}$. The second line should contain the result of float division, $\boldsymbol{a}$ / $\boldsymbol{b}$.  

No rounding or formatting is necessary.

Example 

$\boldsymbol{a}=3$ 

$b=5$  

The result of the integer division $3/5=0$.  
The result of the float division is $3/5=0.6$.  

Print:

0
0.6

Input Format

The first line contains the first integer, $\boldsymbol{a}$. 

The second line contains the second integer, $\boldsymbol{b}$.

Output Format

Print the two lines as described above.  

Sample Input 0
4
3

Sample Output 0
1
1.33333333333
"""

def perform_division(a: int, b: int) -> tuple:
    """
    Performs integer and float division of two integers.

    Parameters:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    tuple: A tuple containing the result of integer division and float division.
    """
    integer_division_result = a // b
    float_division_result = a / b
    return (integer_division_result, float_division_result)