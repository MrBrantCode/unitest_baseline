"""
QUESTION:
Recently Luba learned about a special kind of numbers that she calls beautiful numbers. The number is called beautiful iff its binary representation consists of k + 1 consecutive ones, and then k consecutive zeroes.

Some examples of beautiful numbers:   1_2 (1_10);  110_2 (6_10);  1111000_2 (120_10);  111110000_2 (496_10). 

More formally, the number is beautiful iff there exists some positive integer k such that the number is equal to (2^{k} - 1) * (2^{k} - 1).

Luba has got an integer number n, and she wants to find its greatest beautiful divisor. Help her to find it!


-----Input-----

The only line of input contains one number n (1 ≤ n ≤ 10^5) — the number Luba has got.


-----Output-----

Output one number — the greatest beautiful divisor of Luba's number. It is obvious that the answer always exists.


-----Examples-----
Input
3

Output
1

Input
992

Output
496
"""

def greatest_beautiful_divisor(n: int) -> int:
    """
    Finds the greatest beautiful divisor of the given number n.

    A beautiful number is defined as a number whose binary representation consists of
    k + 1 consecutive ones followed by k consecutive zeroes. This can be represented
    as (2^k - 1) * 2^(k - 1).

    Args:
        n (int): The number for which to find the greatest beautiful divisor.

    Returns:
        int: The greatest beautiful divisor of n.
    """
    beautiful_divisors = []
    for k in range(1, 13):  # 12 is chosen as the upper limit since 2^12 is 4096, which is > 10^5
        temp = (2 ** k - 1) * 2 ** (k - 1)
        if n % temp == 0:
            beautiful_divisors.append(temp)
    return max(beautiful_divisors)