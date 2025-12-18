"""
QUESTION:
Given a total initial investment of $350 distributed between two savings accounts with 6% and 5% annual interest rates, and a cumulative interest of $20 after a year, find the original deposit amounts in each account.

Function name: find_original_deposits
Input: total_investment (float), interest_rate_1 (float), interest_rate_2 (float), total_interest (float)
Output: original_deposit_1 (float), original_deposit_2 (float)
"""

def find_original_deposits(total_investment, interest_rate_1, interest_rate_2, total_interest):
    # Calculate the multiplier for equation (1)
    multiplier = interest_rate_2
    
    # Calculate the adjusted total interest by subtracting the multiplier times total_investment from total_interest
    adjusted_total_interest = total_interest - (multiplier * total_investment)
    
    # Calculate the difference in interest rates
    interest_rate_diff = interest_rate_1 - interest_rate_2
    
    # Calculate the original deposit in the first account
    original_deposit_1 = adjusted_total_interest / interest_rate_diff
    
    # Calculate the original deposit in the second account
    original_deposit_2 = total_investment - original_deposit_1
    
    return original_deposit_1, original_deposit_2