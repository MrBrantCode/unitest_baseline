"""
QUESTION:
Create a function named `debt_to_equity_ratio` that calculates the debt-to-equity ratio given the total amount of debt and equity for a company. The function should return a message indicating whether the ratio is considered healthy, average, or indicative of financial instability. The function should follow these rules: 
- If the ratio is less than 1, the company has a healthy debt-to-equity ratio.
- If the ratio is equal to 1, the company has an average debt-to-equity ratio.
- If the ratio is greater than 1, the company has a high debt-to-equity ratio indicating potential financial instability.
"""

def debt_to_equity_ratio(total_debt, total_equity):
    ratio = total_debt / total_equity
    if ratio < 1:
        return "The company has a healthy debt-to-equity ratio of {}.".format(ratio)
    elif ratio == 1:
        return "The company has a debt-to-equity ratio of 1:1, which is considered average."
    else:
        return "The company has a high debt-to-equity ratio of {}, which indicates potential financial instability.".format(ratio)