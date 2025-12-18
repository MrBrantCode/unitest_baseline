"""
QUESTION:
The positive odd numbers are sorted in ascending order as $1,3,5,7,9,11,13,15,17,19\ldots$, and grouped as $(1),(3,5),(7,9,11),(13,15,17,19),...$ and so on.

Thus, the first group is $\left(1\right)$, the second group is $(3,5)$, the third group is $(7,9,11)$, etc. In general, the $k^{\text{th}}$ group contains the next $\boldsymbol{\mbox{k}}$ elements of the sequence. 

Given $\boldsymbol{\mbox{k}}$, find the sum of the elements of the $k^{\text{th}}$ group. For example, for $k=3$, the answer is $27$:

Complete the function sumOfGroup with input integer $\boldsymbol{\mbox{k}}$.  Return the sum of the elements of the $\boldsymbol{\mbox{k}}$th group.

Constraints

$1\leq k\leq10^6$  

Subtasks  

For $50\%$ of the maximum score, $k\leq10^3$  

Sample Input

$k=3$

Sample Output

$27$

Explanation

We have $k=3$. The $3$rd group is $(7,9,11)$ and the sum of its elements is $7+9+11=27$.
"""

def sumOfGroup(k: int) -> int:
    """
    Calculate the sum of the elements in the k-th group of the sequence of positive odd numbers.

    Parameters:
    k (int): The group number.

    Returns:
    int: The sum of the elements in the k-th group.
    """
    return k ** 3