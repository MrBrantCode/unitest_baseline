"""
QUESTION:
Snuke and Raccoon have a heap of N cards. The i-th card from the top has the integer a_i written on it.
They will share these cards.
First, Snuke will take some number of cards from the top of the heap, then Raccoon will take all the remaining cards.
Here, both Snuke and Raccoon have to take at least one card.
Let the sum of the integers on Snuke's cards and Raccoon's cards be x and y, respectively.
They would like to minimize |x-y|.
Find the minimum possible value of |x-y|.

-----Constraints-----
 - 2 \leq N \leq 2 \times 10^5
 - -10^{9} \leq a_i \leq 10^{9}
 - a_i is an integer.

-----Input-----
Input is given from Standard Input in the following format:
N
a_1 a_2 ... a_{N}

-----Output-----
Print the answer.

-----Sample Input-----
6
1 2 3 4 5 6

-----Sample Output-----
1

If Snuke takes four cards from the top, and Raccoon takes the remaining two cards, x=10, y=11, and thus |x-y|=1. This is the minimum possible value.
"""

def minimize_absolute_difference(a: list[int]) -> int:
    """
    Given a list of integers representing the values on cards, this function calculates
    the minimum possible value of |x - y|, where x is the sum of integers on Snuke's cards
    and y is the sum of integers on Raccoon's cards. Both Snuke and Raccoon must take at
    least one card.

    Parameters:
    a (list[int]): A list of integers representing the values on the cards.

    Returns:
    int: The minimum possible value of |x - y|.
    """
    n = len(a)
    if n < 2:
        raise ValueError("The number of cards must be at least 2.")
    
    lsum = a[0]
    rsum = sum(a[1:])
    ans = abs(lsum - rsum)
    
    for i in range(1, n - 1):
        lsum += a[i]
        rsum -= a[i]
        res = abs(lsum - rsum)
        if res < ans:
            ans = res
    
    return ans