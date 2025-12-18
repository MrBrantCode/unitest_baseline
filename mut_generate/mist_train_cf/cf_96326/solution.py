"""
QUESTION:
Create a function `calculate_tax(income, country, marital_status)` that calculates the amount of tax to be paid based on the inputs of income, country, and marital status. The country can be either "Ireland" or "United States", and the marital status can be either "Single" or "Married". The function should return the calculated tax amount. If any of the inputs are invalid (i.e., income is not a positive integer, country is not "Ireland" or "United States", or marital status is not "Single" or "Married"), the function should return an error message. The tax rates and income brackets for each country are as follows:

- Ireland:
  - Single: 
    - Income up to 20000: 20% tax rate
    - Income between 20001 and 50000: 25% tax rate
    - Income between 50001 and 100000: 30% tax rate
    - Income above 100000: 35% tax rate
  - Married:
    - Income up to 40000: 20% tax rate
    - Income between 40001 and 80000: 25% tax rate
    - Income between 80001 and 150000: 30% tax rate
    - Income above 150000: 35% tax rate

- United States:
  - Single: 
    - Income up to 10000: 10% tax rate
    - Income between 10001 and 50000: 15% tax rate
    - Income between 50001 and 100000: 20% tax rate
    - Income above 100000: 25% tax rate
  - Married:
    - Income up to 20000: 10% tax rate
    - Income between 20001 and 80000: 15% tax rate
    - Income between 80001 and 150000: 20% tax rate
    - Income above 150000: 25% tax rate
"""

def calculate_tax(income, country, marital_status):
    # Check if income is a positive integer
    if not isinstance(income, int) or income < 0:
        return "Error: Income must be a positive integer"
    
    # Check if country is valid
    if country != "Ireland" and country != "United States":
        return "Error: Invalid country"
    
    # Check if marital status is valid
    if marital_status != "Single" and marital_status != "Married":
        return "Error: Invalid marital status"
    
    # Calculate tax based on country and marital status
    if country == "Ireland":
        if marital_status == "Single":
            if income <= 20000:
                tax_rate = 0.20
            elif income <= 50000:
                tax_rate = 0.25
            elif income <= 100000:
                tax_rate = 0.30
            else:
                tax_rate = 0.35
        else:  # Married
            if income <= 40000:
                tax_rate = 0.20
            elif income <= 80000:
                tax_rate = 0.25
            elif income <= 150000:
                tax_rate = 0.30
            else:
                tax_rate = 0.35
    else:  # United States
        if marital_status == "Single":
            if income <= 10000:
                tax_rate = 0.10
            elif income <= 50000:
                tax_rate = 0.15
            elif income <= 100000:
                tax_rate = 0.20
            else:
                tax_rate = 0.25
        else:  # Married
            if income <= 20000:
                tax_rate = 0.10
            elif income <= 80000:
                tax_rate = 0.15
            elif income <= 150000:
                tax_rate = 0.20
            else:
                tax_rate = 0.25
    
    # Calculate and return the amount of tax
    tax_amount = income * tax_rate
    return tax_amount