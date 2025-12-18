"""
QUESTION:
Create a function `calc_net_income` that takes three parameters: `income`, `brackets`, and `deduction`. The `brackets` parameter is a list of tuples representing a progressive tax system, where each tuple contains an income threshold and the corresponding tax rate for income above that threshold. The income thresholds in the list of tuples should be in ascending order. The function should calculate the net income after applying the progressive tax and deduction, and return the result.
"""

def calc_net_income(income, brackets, deduction):
    income -= deduction
    tax = 0
    prev_bracket = 0

    for bracket, rate in brackets:
        if income > bracket:
            tax += rate * (bracket - prev_bracket)
            prev_bracket = bracket
        elif income > prev_bracket:
            tax += rate * (income - prev_bracket)
            prev_bracket = bracket
        else:
            break

    if prev_bracket < income:
        tax += rate * (income - prev_bracket)
    
    return income - tax