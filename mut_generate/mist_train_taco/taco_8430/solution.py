"""
QUESTION:
This challenge is only forPython 2. 

input()

In Python 2, the expression input() is equivalent to eval(raw _input(prompt)).

Code

>>> input()  
1+2
3
>>> company = 'HackerRank'
>>> website = 'www.hackerrank.com'
>>> input()
'The company name: '+company+' and website: '+website
'The company name: HackerRank and website: www.hackerrank.com'

Task  

You are given a polynomial $\mbox{P}$ of a single indeterminate (or variable), $\boldsymbol{x}$. 

You are also given the values of $\boldsymbol{x}$ and $\boldsymbol{\mbox{k}}$. Your task is to verify if $P(x)=k$.

Constraints 

All coefficients of polynomial $\mbox{P}$ are integers. 

$\boldsymbol{x}$ and $y$ are also integers.

Input Format

The first line contains the space separated values of $\boldsymbol{x}$ and $\boldsymbol{\mbox{k}}$. 

The second line contains the polynomial $\mbox{P}$. 

Output Format

Print True if $P(x)=k$. Otherwise, print False.

Sample Input
1 4
x**3 + x**2 + x + 1

Sample Output
True

Explanation

$P(1)=1^3+1^2+1+1=4=k$ 

Hence, the output is True.
"""

def verify_polynomial(x, k, polynomial):
    """
    Verifies if the polynomial P(x) equals k for a given value of x.

    Parameters:
    x (int): The value of the indeterminate x.
    k (int): The value to verify against P(x).
    polynomial (str): The polynomial P in string format.

    Returns:
    bool: True if P(x) equals k, otherwise False.
    """
    try:
        # Replace 'x' in the polynomial with the value of x and evaluate the expression
        result = eval(polynomial.replace('x', str(x)))
        return result == k
    except Exception as e:
        # Handle any potential errors during evaluation
        print(f"Error evaluating polynomial: {e}")
        return False