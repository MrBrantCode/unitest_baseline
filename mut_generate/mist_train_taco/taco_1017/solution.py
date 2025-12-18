"""
QUESTION:
As a token of his gratitude, Takahashi has decided to give his mother an integer sequence. The sequence A needs to satisfy the conditions below:

* A consists of integers between X and Y (inclusive).
* For each 1\leq i \leq |A|-1, A_{i+1} is a multiple of A_i and strictly greater than A_i.



Find the maximum possible length of the sequence.

Constraints

* 1 \leq X \leq Y \leq 10^{18}
* All input values are integers.

Input

Input is given from Standard Input in the following format:


X Y


Output

Print the maximum possible length of the sequence.

Examples

Input

3 20


Output

3


Input

25 100


Output

3


Input

314159265 358979323846264338


Output

31
"""

def max_sequence_length(X, Y):
    n = 1
    while 2 * X <= Y:
        X *= 2
        n += 1
    return n