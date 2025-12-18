"""
QUESTION:
So far, we have only heard of Python's powers. Now, we will witness them!  

Powers or exponents in Python can be calculated using the built-in power function. Call the power function $a^{b}$ as shown below:  

>>> pow(a,b) 

or 

>>> a**b

It's also possible to calculate $a^b\mod m$.  

>>> pow(a,b,m)  

This is very helpful in computations where you have to print the resultant % mod.  

Note: Here, $\boldsymbol{a}$ and $\boldsymbol{b}$ can be floats or negatives, but, if a third argument is present, $\boldsymbol{b}$ cannot be negative.  

Note: Python has a math module that has its own pow(). It takes two arguments and returns a float. It is uncommon to use math.pow().  

Task 

You are given three integers: $\boldsymbol{a}$, $\boldsymbol{b}$, and $m$. Print two lines. 

On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m).  

Input Format 

The first line contains $\boldsymbol{a}$, the second line contains $\boldsymbol{b}$, and the third line contains $m$.  

Constraints 

$1\leq a\leq10$ 

$1\leq b\leq10$ 

$2\leq m\leq1000$  

Sample Input  

3
4
5

Sample Output  

81
1
"""

def calculate_powers_and_mod(a: int, b: int, m: int = None) -> tuple:
    """
    Calculate the power of a to b and the result of a to b modulo m if m is provided.

    Parameters:
    a (int): The base integer.
    b (int): The exponent integer.
    m (int, optional): The modulus integer. Defaults to None.

    Returns:
    tuple: A tuple containing two elements:
           - The first element is the result of a ** b.
           - The second element is the result of pow(a, b, m) if m is provided, otherwise None.
    """
    power_result = a ** b
    mod_result = pow(a, b, m) if m is not None else None
    return (power_result, mod_result)