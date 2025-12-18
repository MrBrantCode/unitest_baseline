"""
QUESTION:
Alice has a positive integer N. She is wondering how many ordered pairs of positive integers (i, j) exist such that i + j = N. 

Help Alice figure out the answer.

Note that since the pairs are ordered, (1, 2) and (2, 1) are considered different.

------ Input Format ------ 

The first and only line of input contains a single integer N.

------ Output Format ------ 

Print a single integer, the number of ordered pairs of positive integers (i, j) such that i + j = N.

------ Constraints ------ 

$1 ≤ N ≤ 100$

----- Sample Input 1 ------ 
1
----- Sample Output 1 ------ 
0
----- explanation 1 ------ 
As both integers must be positive, the minimum sum must be $1 + 1 = 2$. Therefore there are no pairs of positive integers adding up to $1$.

----- Sample Input 2 ------ 
2
----- Sample Output 2 ------ 
1
----- explanation 2 ------ 
$(1,1)$ is the only pair whose sum is $2$. Every other pair has a sum of at least $3$.

----- Sample Input 3 ------ 
3
----- Sample Output 3 ------ 
2
----- explanation 3 ------ 
The two pairs are $(1, 2)$ and $(2, 1)$.
"""

def count_ordered_pairs(N: int) -> int:
    """
    Counts the number of ordered pairs (i, j) of positive integers such that i + j = N.

    Parameters:
    N (int): The sum we are looking for.

    Returns:
    int: The number of ordered pairs (i, j) such that i + j = N.
    """
    if N < 2:
        return 0
    return N - 1