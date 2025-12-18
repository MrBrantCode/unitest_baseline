"""
QUESTION:
Integers in Python can be as big as the bytes in your machine's memory. There is no limit in size as there is: $2^{31}-1$ (c++ int) or $2^{63}-1$ (C++ long long int).    

As we know, the result of $a^{b}$ grows really fast with increasing $\boldsymbol{b}$.  

Let's do some calculations on very large integers.  

Task 

Read four numbers, $\boldsymbol{\alpha}$, $\boldsymbol{b}$, $\boldsymbol{c}$, and $\boldsymbol{d}$, and print the result of $a^b+c^d$.  

Input Format 

Integers $\boldsymbol{\alpha}$, $\boldsymbol{b}$, $\boldsymbol{c}$, and $\boldsymbol{d}$ are given on four separate lines, respectively.

Constraints 

$1\leq a\leq1000$ 

$1\leq b\leq1000$ 

$1\leq c\leq1000$ 

$1\leq d\leq1000$  

Output Format 

Print the result of $a^b+c^d$ on one line.  

Sample Input  

9
29
7
27

Sample Output  

4710194409608608369201743232  

Note: This result is bigger than $2^{63}-1$. Hence, it won't fit in the long long int of C++ or a 64-bit integer.
"""

def calculate_large_integer_sum(a: int, b: int, c: int, d: int) -> int:
    """
    Calculate the sum of two large integer powers.

    Parameters:
    a (int): The base for the first exponentiation.
    b (int): The exponent for the first exponentiation.
    c (int): The base for the second exponentiation.
    d (int): The exponent for the second exponentiation.

    Returns:
    int: The result of the expression a^b + c^d.
    """
    return pow(a, b) + pow(c, d)