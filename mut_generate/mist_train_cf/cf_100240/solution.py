"""
QUESTION:
Create two functions, `calculate_mean_annual_income(prepaids, t_moneys)` and `calculate_average_customers(prepaids, t_moneys)`, that calculate the mean annual income and average number of customers, respectively, for prepaid companies and T-Money. The functions should accept two dictionaries, `prepaids` and `t_moneys`, where each dictionary contains data for the previous three years. The revenue should be expressed in billions and rounded off to two decimal places. The functions should use only loops and arrays for calculations.
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
    
    return {"Prepaid": round(prepaid_average, 2), "T-Money": round(t_money_average, 2)}