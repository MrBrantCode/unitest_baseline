"""
QUESTION:
AtCoder Mart sells 1000000 of each of the six items below:

* Riceballs, priced at 100 yen (the currency of Japan) each
* Sandwiches, priced at 101 yen each
* Cookies, priced at 102 yen each
* Cakes, priced at 103 yen each
* Candies, priced at 104 yen each
* Computers, priced at 105 yen each



Takahashi wants to buy some of them that cost exactly X yen in total. Determine whether this is possible.
(Ignore consumption tax.)

Constraints

* 1 \leq X \leq 100000
* X is an integer.

Input

Input is given from Standard Input in the following format:


X


Output

If it is possible to buy some set of items that cost exactly X yen in total, print `1`; otherwise, print `0`.

Examples

Input

615


Output

1


Input

217


Output

0
"""

def can_buy_exactly(X: int) -> int:
    (q, mod) = divmod(X, 100)
    if 5 * q < mod:
        return 0
    else:
        return 1