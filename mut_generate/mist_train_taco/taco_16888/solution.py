"""
QUESTION:
For a positive integer n

* If n is even, divide by 2.
* If n is odd, multiply by 3 and add 1.



If you repeat the above operation, the result will be 1. A problem called "Colatz conjecture" is that repeating this operation for any positive integer n will always result in 1. This problem is an unsolved problem, also known as the "Kakutani problem" in Japan. It is known that there is no counterexample for a very large number 3 × 253 = 27,021,597,764,222,976 using a computer, but it has not been mathematically proven.

Create a program that takes the integer n as an input and outputs the number of operations that are repeated until the result is 1. The integer n should be an integer that is 1 or more and the value in the middle of repeating the above calculation is 1000000 or less. For example, if you receive 3 as input, the operation column will be


3 → 10 → 5 → 16 → 8 → 4 → 2 → 1


Therefore, 7 is output, which is the number of operations (the number of arrows above).



Input

A sequence of multiple datasets is given as input. The end of the input is indicated by a single line of zeros. One integer n (n ≤ 1000000) is given on one row for each dataset.

The number of datasets does not exceed 50.

Output

Outputs the number of operations for each dataset on one line.

Example

Input

3
10
0


Output

7
6
"""

def collatz_operations(n: int) -> int:
    """
    Calculate the number of operations required to reach 1 using the Collatz conjecture rules.

    Parameters:
    n (int): The starting integer for the Collatz sequence.

    Returns:
    int: The number of operations required to reach 1.
    """
    cnt = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        cnt += 1
    return cnt