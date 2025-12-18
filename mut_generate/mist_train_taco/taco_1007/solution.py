"""
QUESTION:
One of the built-in functions of Python is divmod, which takes two arguments $\boldsymbol{\alpha}$ and $\boldsymbol{b}$ and returns a tuple containing the quotient of $a/b$ first and then the remainder $\boldsymbol{a}$.  

For example:  

>>> print divmod(177,10)
(17, 7)

Here, the integer division is 177/10 => 17 and the modulo operator is 177%10 => 7.

Task 

Read in two integers, $\boldsymbol{a}$ and $\boldsymbol{b}$, and print three lines. 

The first line is the integer division $\boldsymbol{a}//b$ (While using Python2 remember to import division from __future__). 

The second line is the result of the modulo operator: $a\%b$. 

The third line prints the divmod of $\boldsymbol{a}$ and $\boldsymbol{b}$.  

Input Format 

The first line contains the first integer, $\boldsymbol{a}$, and the second line contains the second integer, $\boldsymbol{b}$.   

Output Format 

Print the result as described above.  

Sample Input  

177
10

Sample Output  

17
7
(17, 7)
"""

def perform_divmod_operations(a: int, b: int) -> tuple:
    """
    Perform integer division, modulo operation, and divmod operation on two integers.

    Parameters:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    tuple: A tuple containing:
           - The result of the integer division (a // b)
           - The result of the modulo operation (a % b)
           - The result of the divmod operation (divmod(a, b))
    """
    integer_division = a // b
    modulo_result = a % b
    divmod_result = divmod(a, b)
    
    return (integer_division, modulo_result, divmod_result)