"""
QUESTION:
oneGame function 
This function determines whether Alex wins the stone game given the number of stones in each pile.
The function takes one parameter: piles, a list of integers representing the number of stones in each pile.
Restrictions: piles must be a list of integers, the length of piles must be an even number between 2 and 500, and the total number of stones must be odd.
"""

def stoneGame(piles):
    if not isinstance(piles, list):
        return "Error: Input should be a list."
    
    for i in piles:
        if not isinstance(i, int):
            return "Error: The list should contain only integers."
    
    n = len(piles)
    if n < 2 or n > 500 or n % 2 != 0:
        return "Error: The length of list should be an even number between 2 and 500."
    
    total = sum(piles)
    if total % 2 == 0:
        return "Error: The total number of stones should be odd."
    
    dp = [[0]*n for _ in range(n)]
    for i in range(n): dp[i][i] = piles[i]
    
    for d in range(1, n):
        for i in range(n-d):
            dp[i][i+d] = max(piles[i] - dp[i+1][i+d], piles[i+d] - dp[i][i+d-1])
            
    return dp[0][-1] > 0