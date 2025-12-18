"""
QUESTION:
In a recent [breakthrough] in mathematics, the proof utilized a concept called Height.

Consider a fraction \frac{a}{b}. Its Height is defined as the maximum of its numerator and denominator. So, for example, the Height of \frac{3}{19} would be 19, and the Height of \frac{27}{4} would be 27.

Given a and b, find the Height of \frac{a}{b}.

------ Input Format ------ 

The only line of input contains two integers, a and b.

------ Output Format ------ 

Output a single integer, which is the Height of \frac{a}{b}.

------ Constraints ------ 

$1 ≤ a, b ≤ 100$
$a$ and $b$ do not have any common factors.

----- Sample Input 1 ------ 
3 19

----- Sample Output 1 ------ 
19

----- explanation 1 ------ 
The maximum of $\{3, 19\}$ is $19$. Hence the Height of $\frac{3}{19}$ is $19$.

----- Sample Input 2 ------ 
27 4

----- Sample Output 2 ------ 
27

----- explanation 2 ------ 
The maximum of $\{27, 4\}$ is $27$. Hence the Height of $\frac{27}{4}$ is $27$.
"""

def calculate_height(a: int, b: int) -> int:
    """
    Calculate the Height of a fraction given its numerator and denominator.

    The Height of a fraction \(\frac{a}{b}\) is defined as the maximum of its numerator and denominator.

    Parameters:
    a (int): The numerator of the fraction.
    b (int): The denominator of the fraction.

    Returns:
    int: The Height of the fraction \(\frac{a}{b}\).
    """
    return max(a, b)