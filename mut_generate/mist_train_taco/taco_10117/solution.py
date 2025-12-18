"""
QUESTION:
Snuke found N strange creatures. Each creature has a fixed color and size. The color and size of the i-th creature are represented by i and A_i, respectively.

Every creature can absorb another creature whose size is at most twice the size of itself. When a creature of size A and color B absorbs another creature of size C and color D (C \leq 2 \times A), they will merge into one creature of size A+C and color B. Here, depending on the sizes of two creatures, it is possible that both of them can absorb the other.

Snuke has been watching these creatures merge over and over and ultimately become one creature. Find the number of the possible colors of this creature.

Constraints

* 2 \leq N \leq 100000
* 1 \leq A_i \leq 10^9
* A_i is an integer.

Input

The input is given from Standard Input in the following format:


N
A_1 A_2 … A_N


Output

Print the number of the possible colors of the last remaining creature after the N creatures repeatedly merge and ultimately become one creature.

Examples

Input

3
3 1 4


Output

2


Input

5
1 1 1 1 1


Output

5


Input

6
40 1 30 2 7 20


Output

4
"""

def possible_final_creature_colors(N, A):
    A.sort()
    sumA = sum(A) - A[-1]
    memo = 0
    for i in range(N - 1, -1, -1):
        if sumA * 2 < A[i] or i == 0:
            memo = i
            break
        sumA -= A[i - 1]
    return N - memo