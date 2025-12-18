"""
QUESTION:
Write a function `calculate_tax` that takes an income as input and returns the calculated tax based on the following tax brackets: 
- Any income over $100,000 is taxed at 25%.
- Any income over $60,000 and up to $100,000 is taxed at 20%.
- Any income over $30,000 and up to $60,000 is taxed at 15%.
- Any income over $10,000 and up to $30,000 is taxed at 10%.
- There is no tax on income less than or equal to $10,000.
"""

def calculate_tax(income):
    tax = 0
    
    if income > 100000:
        tax += (income - 100000) * 0.25
        income = 100000
        
    if income > 60000:
        tax += (income - 60000) * 0.20
        income = 60000
        
    if income > 30000:
        tax += (income - 30000) * 0.15
        income = 30000
        
    if income > 10000:
        tax += (income - 10000) * 0.10
        income = 10000

    return tax