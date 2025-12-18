"""
QUESTION:
You've come to your favorite store Infinitesco to buy some ice tea.

The store sells ice tea in bottles of different volumes at different costs. Specifically, a 0.25-liter bottle costs Q yen, a 0.5-liter bottle costs H yen, a 1-liter bottle costs S yen, and a 2-liter bottle costs D yen. The store has an infinite supply of bottles of each type.

You want to buy exactly N liters of ice tea. How many yen do you have to spend?

Constraints

* 1 \leq Q, H, S, D \leq 10^8
* 1 \leq N \leq 10^9
* All input values are integers.

Input

Input is given from Standard Input in the following format:


Q H S D
N


Output

Print the smallest number of yen you have to spend to buy exactly N liters of ice tea.

Examples

Input

20 30 70 90
3


Output

150


Input

10000 1000 100 10
1


Output

100


Input

10 100 1000 10000
1


Output

40


Input

12345678 87654321 12345678 87654321
123456789


Output

1524157763907942
"""

def calculate_minimum_cost(Q, H, S, D, N):
    # Adjust costs to ensure we are always buying the most cost-effective option
    H = min(H, 2 * Q)  # Cost of 0.5L should not be more than twice the cost of 0.25L
    S = min(S, 2 * H)  # Cost of 1L should not be more than twice the cost of 0.5L
    D = min(D, 2 * S)  # Cost of 2L should not be more than twice the cost of 1L
    
    # Calculate the minimum cost
    if N % 2 == 0:
        return (N // 2) * D
    else:
        return (N // 2) * D + S