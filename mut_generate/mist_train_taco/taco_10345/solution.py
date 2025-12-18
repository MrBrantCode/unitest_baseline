"""
QUESTION:
Little penguin Polo loves his home village. The village has n houses, indexed by integers from 1 to n. Each house has a plaque containing an integer, the i-th house has a plaque containing integer p_{i} (1 ≤ p_{i} ≤ n).

Little penguin Polo loves walking around this village. The walk looks like that. First he stands by a house number x. Then he goes to the house whose number is written on the plaque of house x (that is, to house p_{x}), then he goes to the house whose number is written on the plaque of house p_{x} (that is, to house p_{p}_{x}), and so on.

We know that:  When the penguin starts walking from any house indexed from 1 to k, inclusive, he can walk to house number 1.  When the penguin starts walking from any house indexed from k + 1 to n, inclusive, he definitely cannot walk to house number 1.  When the penguin starts walking from house number 1, he can get back to house number 1 after some non-zero number of walks from a house to a house. 

You need to find the number of ways you may write the numbers on the houses' plaques so as to fulfill the three above described conditions. Print the remainder after dividing this number by 1000000007 (10^9 + 7).


-----Input-----

The single line contains two space-separated integers n and k (1 ≤ n ≤ 1000, 1 ≤ k ≤ min(8, n)) — the number of the houses and the number k from the statement.


-----Output-----

In a single line print a single integer — the answer to the problem modulo 1000000007 (10^9 + 7).


-----Examples-----
Input
5 2

Output
54

Input
7 4

Output
1728
"""

def count_plaque_arrangements(n: int, k: int) -> int:
    """
    Calculate the number of ways to write the numbers on the houses' plaques
    such that the conditions specified in the problem are met, modulo 10^9 + 7.

    Parameters:
    n (int): The number of houses.
    k (int): The parameter k from the problem statement.

    Returns:
    int: The number of valid arrangements modulo 10^9 + 7.
    """
    mod = 10**9 + 7
    ans = 1
    
    # Calculate the number of ways for the first k houses
    for i in range(1, k):
        ans = ans * k % mod
    
    # Calculate the number of ways for the remaining houses
    for _ in range(n - k):
        ans = ans * (n - k) % mod
    
    return ans