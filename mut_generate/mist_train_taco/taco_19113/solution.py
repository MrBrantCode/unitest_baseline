"""
QUESTION:
Your friend gives you an equation $A\equiv X^2\pmod{M}$ and asks you to find an integer solution for ${X}$.  

However, you know your friend's mischievous nature and suspect that there is no solution to such an equation. Thus, you first want to find out whether there is a solution to it.  

You may find this link helpful: http://mathworld.wolfram.com/EulersCriterion.html

Input Format

The first line contains the number of cases, ${T}$. ${T}$ lines follow, each containing two integers ${A}$ and ${M}$ separated by a single space.  

Constraints

${0}<T\leq10^5$  
$2\leq M<10^{9}$, ${M}$ is prime  
$0\leq A\lt M$

Output Format

Output ${T}$ lines, each containing one word: YES, if a solution exists and NO otherwise.  

Sample Input
2  
5 7  
4 7

Sample Output
NO  
YES

Explanation

In the second test case, we can take $X=2$, as $4\equiv2^2\pmod{7}$. Or we can take $X=5$, as $5^2=25\equiv4\pmod7$.  

However there is no integer which gives $5$ modulo $7$ when squared.
"""

def has_quadratic_residue(A: int, M: int) -> bool:
    """
    Determines if there exists an integer X such that X^2 ≡ A (mod M).

    Parameters:
    A (int): The integer A in the equation X^2 ≡ A (mod M).
    M (int): The modulus, a prime number.

    Returns:
    bool: True if a solution exists (i.e., "YES"), False otherwise (i.e., "NO").
    """
    if A == 0:
        return True
    return pow(A, (M - 1) // 2, M) == 1