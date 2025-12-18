"""
QUESTION:
There are N turkeys. We number them from 1 through N.

M men will visit here one by one. The i-th man to visit will take the following action:

* If both turkeys x_i and y_i are alive: selects one of them with equal probability, then eats it.
* If either turkey x_i or y_i is alive (but not both): eats the alive one.
* If neither turkey x_i nor y_i is alive: does nothing.



Find the number of pairs (i,\ j) (1 ≤ i < j ≤ N) such that the following condition is held:

* The probability of both turkeys i and j being alive after all the men took actions, is greater than 0.

Constraints

* 2 ≤ N ≤ 400
* 1 ≤ M ≤ 10^5
* 1 ≤ x_i < y_i ≤ N

Input

Input is given from Standard Input in the following format:


N M
x_1 y_1
x_2 y_2
:
x_M y_M


Output

Print the number of pairs (i,\ j) (1 ≤ i < j ≤ N) such that the condition is held.

Examples

Input

3 1
1 2


Output

2


Input

4 3
1 2
3 4
2 3


Output

1


Input

3 2
1 2
1 2


Output

0


Input

10 10
8 9
2 8
4 6
4 9
7 8
2 8
1 8
3 4
3 4
2 7


Output

5
"""

def count_surviving_turkey_pairs(N, M, pairs):
    """
    Calculate the number of pairs (i, j) (1 ≤ i < j ≤ N) such that the probability of both turkeys i and j being alive after all the men took actions is greater than 0.

    Parameters:
    - N (int): The number of turkeys.
    - M (int): The number of men.
    - pairs (list of tuples): A list of tuples where each tuple contains two integers (x_i, y_i) representing the turkeys targeted by each man.

    Returns:
    - int: The number of valid pairs (i, j) such that both turkeys i and j have a non-zero probability of being alive.
    """
    survivors = {v: {v} for v in range(1, N + 1)}
    for (x, y) in reversed(pairs):
        for (v, srv) in survivors.copy().items():
            if x in srv:
                if y in srv:
                    del survivors[v]
                else:
                    srv.add(y)
            elif y in srv:
                srv.add(x)
    return sum((su.isdisjoint(sv) for (su, sv) in combinations(survivors.values(), 2)))