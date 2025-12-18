"""
QUESTION:
Write a function `max_money` that takes three integers A, B, and X as input, representing the denominations of two coins and the target amount of money, respectively. The function should return the maximum amount of money that can be obtained using coins of denominations A and B without exceeding X. Assume that there is an unlimited supply of coins of both denominations.
"""

def max_money(A, B, X):
    max_A = X // A # maximum coins A can be used
    max_B = X // B # maximum coins B can be used
    
    # Try all possible combinations between coins of A and B
    max_money = 0
    for a in range(max_A + 1):
        for b in range(max_B + 1):
            money = a * A + b * B
            if money <= X:
                max_money = max(max_money, money)
  
    return max_money