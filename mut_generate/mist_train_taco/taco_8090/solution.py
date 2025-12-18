"""
QUESTION:
Given is an integer N.
Takahashi chooses an integer a from the positive integers not greater than N with equal probability.
Find the probability that a is odd.

-----Constraints-----
 - 1 \leq N \leq 100

-----Input-----
Input is given from Standard Input in the following format:
N

-----Output-----
Print the probability that a is odd.
Your output will be considered correct when its absolute or relative error from the judge's output is at most 10^{-6}.

-----Sample Input-----
4

-----Sample Output-----
0.5000000000

There are four positive integers not greater than 4: 1, 2, 3, and 4. Among them, we have two odd numbers: 1 and 3. Thus, the answer is \frac{2}{4} = 0.5.
"""

def calculate_odd_probability(N: int) -> float:
    """
    Calculate the probability that a randomly chosen integer from 1 to N is odd.

    Parameters:
    N (int): The upper limit of the range of integers.

    Returns:
    float: The probability that the chosen integer is odd.
    """
    return (N + 1) // 2 / N