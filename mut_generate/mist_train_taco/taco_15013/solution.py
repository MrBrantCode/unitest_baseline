"""
QUESTION:
Snuke has N dogs and M monkeys. He wants them to line up in a row.

As a Japanese saying goes, these dogs and monkeys are on bad terms. ("ken'en no naka", literally "the relationship of dogs and monkeys", means a relationship of mutual hatred.) Snuke is trying to reconsile them, by arranging the animals so that there are neither two adjacent dogs nor two adjacent monkeys.

How many such arrangements there are? Find the count modulo 10^9+7 (since animals cannot understand numbers larger than that). Here, dogs and monkeys are both distinguishable. Also, two arrangements that result from reversing each other are distinguished.

Constraints

* 1 ≤ N,M ≤ 10^5

Input

Input is given from Standard Input in the following format:


N M


Output

Print the number of possible arrangements, modulo 10^9+7.

Examples

Input

2 2


Output

8


Input

3 2


Output

12


Input

1 8


Output

0


Input

100000 100000


Output

530123477
"""

def count_valid_arrangements(N, M):
    MOD = 1000000007
    
    # Determine the smaller and larger of the two numbers
    n = min(N, M)
    m = max(N, M)
    
    # If the difference between the larger and smaller is more than 1, no valid arrangement is possible
    if m > n + 1:
        return 0
    
    # Calculate factorial of n and m
    def factorial(x):
        result = 1
        for i in range(1, x + 1):
            result = result * i % MOD
        return result
    
    # Calculate the number of valid arrangements
    if m == n + 1:
        # If m is exactly one more than n, we can arrange them in a valid way
        ans = factorial(n)
        ans = ans * factorial(m) % MOD
    elif m == n:
        # If m is equal to n, we can arrange them in a valid way with two possible starting points
        ans = 2 * factorial(n) * factorial(m) % MOD
    else:
        # This case should not occur due to the previous check
        ans = 0
    
    return ans