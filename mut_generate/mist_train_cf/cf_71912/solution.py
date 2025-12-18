"""
QUESTION:
Write a function `fertilizer_combinations(n)` to compute the optimal combination(s) of fertilizer bags that sum up to `n` pounds of nitrogen. There are three types of fertilizer bags available: Type 1 (3lbs), Type 2 (5lbs), and Type 3 (7lbs). The function should return all combinations that minimize the total weight of the fertilizer bags, or an error message if no combination can exactly achieve `n` pounds of nitrogen.
"""

def fertilizer_combinations(n):
    if n < 3:
        return "No combination can exactly achieve the needed {}lbs of nitrogen".format(n)

    combinations = []  
    min_bags = float('inf')

    for i in range(n // 7 + 1):
        for j in range(n // 5 + 1):
            residual = n - i * 7 - j * 5
            if residual >= 0 and residual % 3 == 0:
                if i + j + residual // 3 < min_bags:
                    min_bags = i + j + residual // 3
                    combinations = [[residual // 3, j, i]]
                elif i + j + residual // 3 == min_bags:
                    combinations.append([residual // 3, j, i])
    return combinations