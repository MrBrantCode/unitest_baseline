"""
QUESTION:
The factorial of the integer $n$, written $n!$, is defined as:   

$n!=n\times(n-1)\times(n-2)\times\text{}\cdots\times3\times2\times1$

Calculate and print the factorial of a given integer.  

For example, if $n=30$, we calculate $30\times29\times28\times\text{...}\times2\times1$ and get $265252859812191058636308480000000$.

Function Description

Complete the extraLongFactorials function in the editor below.  It should print the result and return.  

extraLongFactorials has the following parameter(s):  

n: an integer

Note: Factorials of $n>20$ can't be stored even in a $64-bit$ long long variable. Big integers must be used for such calculations. Languages like Java, Python, Ruby etc. can handle big integers, but we need to write additional code in C/C++ to handle huge values.  

We recommend solving this challenge using BigIntegers.  

Input Format

Input consists of a single integer $n$

Constraints

$1\leq n\leq100$

Output Format

Print the factorial of $n$. 

Sample Input

$25$

Sample Output

$1551121004330985984000000$

Explanation

$25!=25\times24\times23\times\text{...}\times3\times2\times1$
"""

from math import factorial

def calculate_factorial(n: int) -> str:
    """
    Calculate the factorial of a given integer n.

    Parameters:
    n (int): The integer for which the factorial is to be calculated.

    Returns:
    str: The factorial of n as a string.
    """
    return str(factorial(n))