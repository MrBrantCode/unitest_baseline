"""
QUESTION:
We have two indistinguishable pieces placed on a number line. Both pieces are initially at coordinate 0. (They can occupy the same position.)

We can do the following two kinds of operations:

* Choose a piece and move it to the right (the positive direction) by 1.
* Move the piece with the smaller coordinate to the position of the piece with the greater coordinate. If two pieces already occupy the same position, nothing happens, but it still counts as doing one operation.



We want to do a total of N operations of these kinds in some order so that one of the pieces will be at coordinate A and the other at coordinate B. Find the number of ways to move the pieces to achieve it. The answer can be enormous, so compute the count modulo 998244353.

Two ways to move the pieces are considered different if and only if there exists an integer i (1 \leq i \leq N) such that the set of the coordinates occupied by the pieces after the i-th operation is different in those two ways.

Constraints

* 1 \leq N \leq 10^7
* 0 \leq A \leq B \leq N
* All values in input are integers.

Input

Input is given from Standard Input in the following format:


N A B


Output

Print the number of ways to move the pieces to achieve our objective, modulo 998244353.

Examples

Input

5 1 3


Output

4


Input

10 0 0


Output

1


Input

10 4 6


Output

197


Input

1000000 100000 200000


Output

758840509
"""

def count_ways_to_move_pieces(N: int, A: int, B: int) -> int:
    M = 998244353
    P = N + 1
    f = 1
    F = [1] * P
    I = [1] * P
    z = 0
    R = range
    
    for n in R(1, P):
        F[n] = f = f * n % M
    
    I[N] = i = pow(f, M - 2, M)
    
    for n in R(N, 1, -1):
        I[n - 1] = i = i * n % M
    
    for k in R(min(A + 1, N - B) if N - B - A else A + 1):
        Q = N - B - k - 1
        z = (z + (B - k) * F[B + k - 1] * I[B] * I[k] * F[Q + A - k] * I[Q] * I[A - k]) % M
    
    return z if B else 1