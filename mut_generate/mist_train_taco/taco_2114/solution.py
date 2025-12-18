"""
QUESTION:
A continued fraction of height n is a fraction of form $a_{1} + \frac{1}{a_{2} + \frac{1}{\ldots + \frac{1}{a_{n}}}}$. You are given two rational numbers, one is represented as [Image] and the other one is represented as a finite fraction of height n. Check if they are equal.


-----Input-----

The first line contains two space-separated integers p, q (1 ≤ q ≤ p ≤ 10^18) — the numerator and the denominator of the first fraction.

The second line contains integer n (1 ≤ n ≤ 90) — the height of the second fraction. The third line contains n space-separated integers a_1, a_2, ..., a_{n} (1 ≤ a_{i} ≤ 10^18) — the continued fraction.

Please, do not use the %lld specifier to read or write 64-bit integers in С++. It is preferred to use the cin, cout streams or the %I64d specifier.


-----Output-----

Print "YES" if these fractions are equal and "NO" otherwise.


-----Examples-----
Input
9 4
2
2 4

Output
YES

Input
9 4
3
2 3 1

Output
YES

Input
9 4
3
1 2 4

Output
NO



-----Note-----

In the first sample $2 + \frac{1}{4} = \frac{9}{4}$.

In the second sample $2 + \frac{1}{3 + \frac{1}{1}} = 2 + \frac{1}{4} = \frac{9}{4}$.

In the third sample $1 + \frac{1}{2 + \frac{1}{4}} = \frac{13}{9}$.
"""

from fractions import Fraction

def are_fractions_equal(p: int, q: int, n: int, a: list) -> str:
    """
    Determines if a given rational number (p/q) is equal to a continued fraction of height n.

    Parameters:
    p (int): The numerator of the first fraction.
    q (int): The denominator of the first fraction.
    n (int): The height of the continued fraction.
    a (list): A list of integers representing the continued fraction.

    Returns:
    str: "YES" if the fractions are equal, "NO" otherwise.
    """
    # Reverse the list to process the continued fraction correctly
    a.reverse()
    
    # Initialize the result with the first element of the continued fraction
    res = Fraction(a[0], 1)
    
    # Compute the continued fraction
    for i in range(1, n):
        res = a[i] + 1 / res
    
    # Compare the computed continued fraction with the given fraction (p/q)
    return 'YES' if res == Fraction(p, q) else 'NO'