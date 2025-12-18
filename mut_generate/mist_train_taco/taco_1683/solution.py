"""
QUESTION:
To make it difficult to withdraw money, a certain bank allows its customers to withdraw only one of the following amounts in one operation:
 - 1 yen (the currency of Japan)
 - 6 yen, 6^2(=36) yen, 6^3(=216) yen, ...
 - 9 yen, 9^2(=81) yen, 9^3(=729) yen, ...
At least how many operations are required to withdraw exactly N yen in total?
It is not allowed to re-deposit the money you withdrew.

-----Constraints-----
 - 1 \leq N \leq 100000
 - N is an integer.

-----Input-----
Input is given from Standard Input in the following format:
N

-----Output-----
If at least x operations are required to withdraw exactly N yen in total, print x.

-----Sample Input-----
127

-----Sample Output-----
4

By withdrawing 1 yen, 9 yen, 36(=6^2) yen and 81(=9^2) yen, we can withdraw 127 yen in four operations.
"""

def minimum_withdrawal_operations(N: int) -> int:
    # List of possible withdrawal amounts
    withdrawal_amounts = [1, 6, 9, 36, 81, 216, 729, 1296, 6561, 7776, 46656, 59049]
    
    # Initialize a list to store the minimum operations required for each amount up to N
    min_operations = [0] * (N + 1)
    
    # Fill the min_operations list using dynamic programming
    for i in range(1, N + 1):
        mn = float('inf')
        for amount in withdrawal_amounts:
            if i - amount >= 0:
                mn = min(mn, min_operations[i - amount] + 1)
        min_operations[i] = mn
    
    return min_operations[N]