"""
QUESTION:
Ikta loves fast programs. Recently, I'm trying to speed up the division program. However, it doesn't get much faster, so I thought it would be better to make it faster only for "common sense and typical" inputs. The problem Ikta is trying to solve is as follows.

For a given non-negative integer n, divide p (n) − 1-digit positive integer 11 ... 1 by p (n) in decimal notation. However, p (n) represents the smallest prime number larger than 22 {... 2} (n 2). Let p (0) = 2.

Your job is to complete the program faster than Ikta.



Input

The input is given in the following format.


n


Given the non-negative integer n of the input in question.

Constraints

Each variable being input satisfies the following constraints.

* 0 ≤ n <1000

Output

Print the solution to the problem on one line.

Examples

Input

0


Output

1


Input

1


Output

2


Input

2


Output

1
"""

def fast_division_result(n: int) -> int:
    if n == 0:
        return 1
    elif n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return 0