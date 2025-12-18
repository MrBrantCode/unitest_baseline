"""
QUESTION:
Write a function named `advanced_factor_combinations(n)` that generates all combinations of factors of the input integer `n` within the range `[2, n - 1]`. Then, for each combination, filter out the combinations where the sum of factors is not a prime number. Finally, for the remaining combinations, discard those where the product of factors is not a perfect square. The function should return a list of valid combinations.

Restrictions: `1 <= n <= 108` and the function should use depth-first search to generate factor combinations.
"""

import math

def advanced_factor_combinations(n):
    def is_prime(num):
        if num < 2: return False
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True

    def is_square(num):
        return math.isqrt(num) ** 2 == num  

    def dfs(start, comb, num):
        if num == 1 and is_prime(sum(comb)) and is_square(math.prod(comb)):
            res.append(comb)
            return
        for i in range(start, int(math.sqrt(num))+1):
            if num % i == 0:
                dfs(i, comb + [i], num // i)

    res = []
    dfs(2, [], n)
    return res