"""
QUESTION:
B: Ebi-chan and Integer Sequences-

problem

Ebi-chan likes sequences. I especially like arithmetic progressions. This time, I decided to create a sequence that meets the following conditions.

* Arithmetic progression of length n
* When the i-th element of the sequence is defined as s_i, all s_i (1 \ leq i \ leq n) are integers that satisfy 0 \ leq s_i \ leq m.



How many sequences are there that satisfy the above conditions? However, the answer can be very large, so print the remainder after dividing by 10 ^ 9 + 7.

Input format

Input is given in one line.


n m

n represents the length of the sequence.

Constraint

* 1 \ leq n \ leq 10 ^ {15}
* 0 \ leq m \ leq 10 ^ {15}



Output format

Divide the number of arithmetic progressions that satisfy the condition by 10 ^ 9 + 7 and output the remainder in one row.

Input example 1


3 9

Output example 1


50

Input example 2


10000000000 10000000000

Output example 2


999999942

Note that the input does not fit in a 32-bit integer.





Example

Input

3 9


Output

50
"""

def count_arithmetic_progressions(n: int, m: int) -> int:
    MOD = 10 ** 9 + 7

    def sum_arithmetic_progression(a: int, d: int, n: int) -> int:
        return n * (2 * a + (n - 1) * d) // 2

    if n == 1:
        return (m + 1) % MOD
    else:
        s = sum_arithmetic_progression(m + 1, -n + 1, 1 + m // (n - 1))
        s *= 2
        s -= m + 1
        return s % MOD