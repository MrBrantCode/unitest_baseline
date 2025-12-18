"""
QUESTION:
In an electric circuit, when two resistors R_1 and R_2 are connected in parallel, the equivalent resistance R_3 can be derived from the following formula:

* \frac{1}{R_1} + \frac{1}{R_2} = \frac{1}{R_3}



Given R_1 and R_2, find R_3.

Constraints

* 1 \leq R_1, R_2 \leq 100
* R_1 and R_2 are integers.

Input

The input is given from Standard Input in the following format:


R_1 R_2


Output

Print the value of R_3.

The output is considered correct if the absolute or relative error is at most 10^{-6}.

Examples

Input

2 3


Output

1.2000000000


Input

100 99


Output

49.7487437186
"""

def calculate_parallel_resistance(r1: int, r2: int) -> float:
    """
    Calculate the equivalent resistance of two resistors connected in parallel.

    Parameters:
    r1 (int): The resistance value of the first resistor.
    r2 (int): The resistance value of the second resistor.

    Returns:
    float: The equivalent resistance when the two resistors are connected in parallel.
    """
    return r1 * r2 / (r1 + r2)