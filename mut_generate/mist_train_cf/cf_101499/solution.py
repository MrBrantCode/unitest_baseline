"""
QUESTION:
Create a function named `debt_to_equity_ratio` that takes in two parameters: `total_debt` and `total_equity`. The function should calculate the debt-to-equity ratio by dividing `total_debt` by `total_equity`. Based on the ratio, return a message indicating whether the company is financially stable or not. The message should include the ratio value. 

The function should return "The company has a healthy debt-to-equity ratio of {}." if the ratio is less than 1, "The company has a debt-to-equity ratio of 1:1, which is considered average." if the ratio equals 1, and "The company has a high debt-to-equity ratio of {}, which indicates potential financial instability." if the ratio is greater than 1.
"""

def debt_to_equity_ratio(total_debt, total_equity):
    ratio = total_debt / total_equity
    if ratio < 1:
        return "The company has a healthy debt-to-equity ratio of {}.".format(ratio)
    elif ratio == 1:
        return "The company has a debt-to-equity ratio of 1:1, which is considered average."
    else:
        return "The company has a high debt-to-equity ratio of {}, which indicates potential financial instability.".format(ratio)