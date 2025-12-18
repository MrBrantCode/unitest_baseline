"""
QUESTION:
Create a function called `calculate_tax` that takes in three parameters: `income`, `country`, and `marital_status`. The function should return the amount of tax to be paid based on the given income, country, and marital status, using the following tax rates and income brackets:

- For Ireland: 
  - Single: 
    - Income up to 20000: 20% tax rate
    - Income between 20001 and 50000: 25% tax rate
    - Income above 50000: 30% tax rate
  - Married:
    - Income up to 40000: 20% tax rate
    - Income between 40001 and 80000: 25% tax rate
    - Income above 80000: 30% tax rate
- For United States:
  - Single: 
    - Income up to 10000: 10% tax rate
    - Income between 10001 and 50000: 15% tax rate
    - Income above 50000: 20% tax rate
  - Married:
    - Income up to 20000: 10% tax rate
    - Income between 20001 and 100000: 15% tax rate
    - Income above 100000: 20% tax rate

Note that the `country` parameter can only be "Ireland" or "United States", and the `marital_status` parameter can only be "Single" or "Married".
"""

def calculate_tax(income, country, marital_status):
    if country == "Ireland":
        if marital_status == "Single":
            if income <= 20000:
                tax_rate = 0.2
            elif income <= 50000:
                tax_rate = 0.25
            else:
                tax_rate = 0.3
        elif marital_status == "Married":
            if income <= 40000:
                tax_rate = 0.2
            elif income <= 80000:
                tax_rate = 0.25
            else:
                tax_rate = 0.3
    elif country == "United States":
        if marital_status == "Single":
            if income <= 10000:
                tax_rate = 0.1
            elif income <= 50000:
                tax_rate = 0.15
            else:
                tax_rate = 0.2
        elif marital_status == "Married":
            if income <= 20000:
                tax_rate = 0.1
            elif income <= 100000:
                tax_rate = 0.15
            else:
                tax_rate = 0.2
    tax_amount = income * tax_rate
    return tax_amount