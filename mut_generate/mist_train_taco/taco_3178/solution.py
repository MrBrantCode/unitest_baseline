"""
QUESTION:
There are N bags of biscuits. The i-th bag contains A_i biscuits.

Takaki will select some of these bags and eat all of the biscuits inside. Here, it is also possible to select all or none of the bags.

He would like to select bags so that the total number of biscuits inside is congruent to P modulo 2. How many such ways to select bags there are?

Constraints

* 1 \leq N \leq 50
* P = 0 or 1
* 1 \leq A_i \leq 100

Input

Input is given from Standard Input in the following format:


N P
A_1 A_2 ... A_N


Output

Print the number of ways to select bags so that the total number of biscuits inside is congruent to P modulo 2.

Examples

Input

2 0
1 3


Output

2


Input

1 1
50


Output

0


Input

3 0
1 1 1


Output

4


Input

45 1
17 55 85 55 74 20 90 67 40 70 39 89 91 50 16 24 14 43 24 66 25 9 89 71 41 16 53 13 61 15 85 72 62 67 42 26 36 66 4 87 59 91 4 25 26


Output

17592186044416
"""

def count_biscuit_selections(N, P, A):
    # Calculate the number of odd and even bags
    O = sum([a % 2 for a in A])
    E = N - O
    
    # Precompute factorials up to 50
    fa = [1]
    for i in range(1, 51):
        fa.append(fa[-1] * i)
    
    # Calculate the number of valid selections
    ans = 0
    for i in range(P, O + 1, 2):
        ans += fa[O] // (fa[i] * fa[O - i])
    
    # Multiply by the number of ways to choose even bags
    return ans * 2 ** E