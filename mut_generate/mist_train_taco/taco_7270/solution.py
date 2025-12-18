"""
QUESTION:
Having learned the multiplication table, Takahashi can multiply two integers between 1 and 9 (inclusive) together.
Given an integer N, determine whether N can be represented as the product of two integers between 1 and 9. If it can, print Yes; if it cannot, print No.

-----Constraints-----
 - 1 \leq N \leq 100
 - N is an integer.

-----Input-----
Input is given from Standard Input in the following format:
N

-----Output-----
If N can be represented as the product of two integers between 1 and 9 (inclusive), print Yes; if it cannot, print No.

-----Sample Input-----
10

-----Sample Output-----
Yes

10 can be represented as, for example, 2 \times 5.
"""

def can_be_product_of_two_integers(N: int) -> str:
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == N:
                return 'Yes'
    return 'No'