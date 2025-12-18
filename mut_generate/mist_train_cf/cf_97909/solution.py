"""
QUESTION:
Create two functions, `calculate_mean_annual_income` and `calculate_average_customers`, that take two dictionaries of financial data for prepaid companies and T-Money as input. The dictionaries should be in the format `{"year": {"revenue": amount, "customers": number}}`. The functions should calculate the mean annual income and average number of customers, respectively, for the previous three years. The calculations should be performed using only loops and arrays, and the results should be expressed in billions for revenue (rounded to two decimal places) and exact numbers for customers. The output should be a dictionary with the mean or average values for prepaid companies and T-Money.
"""

def calculate_mean_annual_income(prepaids, t_moneys):
    prepaid_revenues = []
    t_money_revenues = []
    
    for year in sorted(prepaids.keys(), reverse=True)[:3]:
        prepaid_revenues.append(prepaids[year]["revenue"])
        
    for year in sorted(t_moneys.keys(), reverse=True)[:3]:
        t_money_revenues.append(t_moneys[year]["revenue"])
    
    prepaid_mean = sum(prepaid_revenues) / len(prepaid_revenues) / 1000
    t_money_mean = sum(t_money_revenues) / len(t_money_revenues) / 1000
    
    return {"Prepaid": round(prepaid_mean, 2), "T-Money": round(t_money_mean, 2)}

def calculate_average_customers(prepaids, t_moneys):
    prepaid_customers = []
    t_money_customers = []
    
    for year in sorted(prepaids.keys(), reverse=True)[:3]:
        prepaid_customers.append(prepaids[year]["customers"])
        
    for year in sorted(t_moneys.keys(), reverse=True)[:3]:
        t_money_customers.append(t_moneys[year]["customers"])
    
    prepaid_average = sum(prepaid_customers) / len(prepaid_customers)
    t_money_average = sum(t_money_customers) / len(t_money_customers)
    
    return {"Prepaid": round(prepaid_average), "T-Money": round(t_money_average)}