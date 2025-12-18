"""
QUESTION:
Takahashi bought a piece of apple pie at ABC Confiserie. According to his memory, he paid N yen (the currency of Japan) for it.

The consumption tax rate for foods in this shop is 8 percent. That is, to buy an apple pie priced at X yen before tax, you have to pay X \times 1.08 yen (rounded down to the nearest integer).

Takahashi forgot the price of his apple pie before tax, X, and wants to know it again. Write a program that takes N as input and finds X. We assume X is an integer.

If there are multiple possible values for X, find any one of them. Also, Takahashi's memory of N, the amount he paid, may be incorrect. If no value could be X, report that fact.

Constraints

* 1 \leq N \leq 50000
* N is an integer.

Input

Input is given from Standard Input in the following format:


N


Output

If there are values that could be X, the price of the apple pie before tax, print any one of them.
If there are multiple such values, printing any one of them will be accepted.
If no value could be X, print `:(`.

Examples

Input

432


Output

400


Input

1079


Output

:(


Input

1001


Output

927
"""

def find_pre_tax_price(N: int) -> int or str:
    m = 1
    while int(m * 1.08) < N:
        m += 1
    return m if int(m * 1.08) == N else ':('