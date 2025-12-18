"""
QUESTION:
Function `f(n, k)` denotes the number of winning positions for Alice on her initial turn, given the parameters `n` (the total number of stones) and `k` (the maximum number of piles a stone can be divided into). Define another function `g(n)` as the sum of `f(n, k)` for all `2 ≤ k ≤ n`. Determine the value of `g(200) mod (10^9 + 7)`. 

The function should follow these rules: 

- During each player's turn, they must select a pile containing at least 2 stones and execute a split operation, dividing the chosen pile into a random set of `p` non-empty piles of arbitrary sizes, where `2 ≤ p ≤ k` for a certain fixed constant `k`. 
- A winning position is characterized as a set of stone piles where a player can guarantee victory regardless of the opponent's moves.
"""

def g(n, M=10**9 + 7):
    """
    Calculate the sum of f(n, k) for all 2 ≤ k ≤ n, 
    where f(n, k) denotes the number of winning positions for Alice on her initial turn, 
    given the parameters n (the total number of stones) and k (the maximum number of piles a stone can be divided into).
    
    Args:
        n (int): The total number of stones.
        M (int): The modulus. Defaults to 10^9 + 7.
    
    Returns:
        int: The sum of f(n, k) for all 2 ≤ k ≤ n, modulo M.
    """
    
    # Initialize variables to store Hamming weight and odd values
    hammingweight = [0]*(n + 1)
    odd = [0]*(n + 1)
    
    # Calculate Hamming weight and odd values
    odd[1] = 1
    for i in range(2, n + 1):
        if i & 1 == 0:
            hammingweight[i] = hammingweight[i // 2]
        else:
            hammingweight[i] = hammingweight[i - 1] + 1
        odd[i] = 1 - odd[hammingweight[i]]
    
    # Initialize variable to store the count of winning positions
    count = [0]*(n + 1)
    
    # Calculate the count of winning positions
    for k in range(2, n + 1):
        for i in range(k, n + 1):
            count[i] = (count[i] + odd[i - k + 1]) % M
    
    # Return the sum of the count of winning positions modulo M
    return sum(count) % M