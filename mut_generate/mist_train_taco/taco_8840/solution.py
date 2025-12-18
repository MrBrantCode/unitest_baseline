"""
QUESTION:
On the eve of Diwali, Hari is decorating his house with a serial light bulb set. The serial light bulb set has N bulbs placed sequentially on a string which is programmed to change patterns every second. If at least one bulb in the set is on at any given instant of time, how many different patterns of light can the serial light bulb set produce? 

Note: Lighting two bulbs *-* is different from **- 

Input Format 

The first line contains the number of test cases T, T lines follow. 

Each line contains an integer N, the number of bulbs in the serial light bulb set. 

Output Format 

Print the total number of patterns modulo 10^{5}

Constraints 

1 <= T <= 1000 

0< N < 10^{4}

Sample Input

2
1
2

Sample Output

1
3

Explanation

Case 1: 1 bulb can be lit in only 1 way. 

Case 2: 2 bulbs can be lit in -*, *-, ** i.e. 3 ways.
"""

def calculate_light_patterns(n: int) -> int:
    """
    Calculate the total number of patterns of light a serial light bulb set can produce,
    given the number of bulbs, modulo 100000.

    Parameters:
    n (int): The number of bulbs in the serial light bulb set.

    Returns:
    int: The total number of patterns modulo 100000.
    """
    if n == 0:
        return 0
    return (2 ** n - 1) % 100000