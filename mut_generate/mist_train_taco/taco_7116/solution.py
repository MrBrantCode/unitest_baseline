"""
QUESTION:
Apart from Nian, there is a daemon named Sui, which terrifies children and causes them to become sick. Parents give their children money wrapped in red packets and put them under the pillow, so that when Sui tries to approach them, it will be driven away by the fairies inside.

Big Banban is hesitating over the amount of money to give out. He considers loops to be lucky since it symbolizes unity and harmony.

He would like to find a positive integer n not greater than 10^18, such that there are exactly k loops in the decimal representation of n, or determine that such n does not exist.

A loop is a planar area enclosed by lines in the digits' decimal representation written in Arabic numerals. For example, there is one loop in digit 4, two loops in 8 and no loops in 5. Refer to the figure below for all exact forms.

 $0123456789$ 


-----Input-----

The first and only line contains an integer k (1 ≤ k ≤ 10^6) — the desired number of loops.


-----Output-----

Output an integer — if no such n exists, output -1; otherwise output any such n. In the latter case, your output should be a positive decimal integer not exceeding 10^18.


-----Examples-----
Input
2

Output
462
Input
6

Output
8080
"""

def find_lucky_number_with_loops(k: int) -> int:
    """
    Finds a positive integer n not greater than 10^18 such that there are exactly k loops
    in the decimal representation of n, or determines that such n does not exist.

    Args:
        k (int): The desired number of loops.

    Returns:
        int: A positive integer n with exactly k loops, or -1 if no such n exists.
    """
    if k > 36:
        return -1
    
    if k % 2 == 0:
        return int('8' * (k // 2))
    else:
        return int('4' + '8' * (k // 2))