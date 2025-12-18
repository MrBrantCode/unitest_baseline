"""
QUESTION:
Implement a function `calculate_earnings` that takes an array of stock prices as input, calculates the total amount of money earned from buying and selling stocks on consecutive days with a maximum of 2 transactions, and returns the maximum possible amount of money earned after deducting a $0.50 transaction fee for each transaction. The function should only consider transactions where the buy and sell occur on consecutive days.
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