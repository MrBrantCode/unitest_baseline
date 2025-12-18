"""
QUESTION:
Create a function `correct_interest_calculator` that takes the initial investment amount and the total interest earned after one year as inputs, and returns the amount invested in a 5% annual interest account and a 7% annual interest account. The function should iterate over all possible proportions of the investment and return the correct amounts when the calculated total interest matches the given total interest.
"""

def correct_interest_calculator(investment, total_interest):
  # Loop through each possible proportion for the five_percent_account
  for i in range(0, investment + 1):
    five_percent_account = i
    seven_percent_account = investment - i
    calculated_interest = five_percent_account * 0.05 + seven_percent_account * 0.07
  
    # When the calculated interest matches the given total interest, the function returns the investment of each account
    if calculated_interest == total_interest:
      return five_percent_account, seven_percent_account
      
  # If no investment proportions match the given total_interest, the function returns an error
  return "No suitable investment allocation found."