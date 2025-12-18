"""
QUESTION:
Implement a function `calculate_earnings(arr)` that calculates the total amount of money earned from a given array of stock prices, where the function only includes the stock prices that were bought and sold on consecutive days and the maximum number of consecutive buy-sell transactions allowed is limited to 2. The function should also account for transaction fees, where a fixed fee of $0.50 is deducted from the total amount earned for each transaction. The function should return the maximum possible amount of money earned after considering these fees.
"""

def calculate_earnings(arr):
    n = len(arr)
    if n < 2:
        return 0
    
    max_earnings = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            earnings = arr[j] - arr[i] - 0.5  # Subtract transaction fee
            if earnings > 0:
                remaining_arr = arr[j+1:]
                max_remaining_earnings = calculate_earnings(remaining_arr)
                total_earnings = earnings + max_remaining_earnings
                max_earnings = max(max_earnings, total_earnings)
    
    return max_earnings