"""
QUESTION:
Problem statement

Meatishi can increase or decrease the number of fingers.
There are n buns in front of Nikunishi-kun.
Meatishi is trying to count the number of steamed buns by breaking his finger.
There are only two shapes that Nishikun's fingers can take, whether they are broken or not.
Nikunishi understands binary numbers.
Nikunishi-kun can count numbers by associating each finger with a binary digit.
Nikunishi doesn't understand the logarithm.
Find the minimum number of fingers needed to count the buns instead of Nishikun.

input


n


Constraint

* An integer
* 0 ≤ n ≤ 1018



output

Print the answer on one line, and print a newline at the end.

sample

Sample input 1


0


Sample output 1


0


Sample input 2


Four


Sample output 2


3


Sample input 3


31


Sample output 3


Five


Sample input 4


36028797018963968


Sample output 4


56






Example

Input

0


Output

0
"""

def calculate_minimum_fingers(n: int) -> int:
    """
    Calculate the minimum number of fingers needed to count the buns.

    Parameters:
    n (int): The number of buns.

    Returns:
    int: The minimum number of fingers needed.
    """
    if n == 0:
        return 0
    else:
        return len(str(bin(n))[2:])