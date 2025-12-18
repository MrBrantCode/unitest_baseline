"""
QUESTION:
Check Tutorial tab to know how to solve.  

Task 

Given an integer, $n$, perform the following conditional actions:

If $n$ is odd, print Weird
If $n$ is even and in the inclusive range of $2$ to $5$, print Not Weird
If $n$ is even and in the inclusive range of $\boldsymbol{6}$ to $\textbf{20}$, print Weird
If $n$ is even and greater than $\textbf{20}$, print Not Weird

Input Format

A single line containing a positive integer, $n$.

Constraints

$1\leq n\leq100$

Output Format

Print Weird if the number is weird.  Otherwise, print Not Weird.

Sample Input 0
3

Sample Output 0
Weird

Explanation 0

$n=3$ 

$n$ is odd and odd numbers are weird, so print Weird.

Sample Input 1
24

Sample Output 1
Not Weird

Explanation 1

$n=24$ 

$n>20$ and $n$ is even, so it is not weird.
"""

def check_weirdness(n: int) -> str:
    if n < 1 or n > 100:
        raise ValueError("n must be between 1 and 100 inclusive")
    
    if n % 2 != 0:
        return 'Weird'
    elif n >= 2 and n <= 5 or n > 20:
        return 'Not Weird'
    else:
        return 'Weird'