"""
QUESTION:
Create a function named `verify_sales_and_clicks` that takes a dictionary `data` as input, where the dictionary represents a table with columns 'Campaign', 'Date', 'Time', 'Sales', and 'Clicks'. The function should verify if the total sales for the 'Spring' and 'Summer' campaigns is exactly equal to $50 and if the number of clicks for each of these campaigns is greater than or equal to 100. The function should return `True` if both conditions are satisfied and `False` otherwise.
"""

import pandas as pd

def verify_sales_and_clicks(data):
    """
    Verify if the total sales for the Spring and Summer campaigns on FirstPromoter.com are exactly equal to $50.
    Additionally, the function must verify if the number of clicks for the Spring and Summer campaigns is
    greater than or equal to 100. It should not consider the sales and clicks for the Fall and Winter campaigns.
    The input table 'data' must include the specific dates and hours of each campaign.
    """
    
    # Create a pandas dataframe from the input table
    df = pd.DataFrame(data)

    # Filter the dataframe to consider only the Spring and Summer campaigns
    df_ss = df[(df['Campaign'] == 'Spring') | (df['Campaign'] == 'Summer')]

    # Verify if the total sales for the Spring and Summer campaigns is exactly equal to $50
    total_sales = df_ss['Sales'].sum()
    if total_sales != 50:
        return False

    # Verify if the number of clicks for the Spring and Summer campaigns is greater than or equal to 100
    df_ss_clicks = df_ss.groupby(['Campaign']).sum()['Clicks']
    if (df_ss_clicks < 100).any():
        return False

    # Return True if both conditions are satisfied
    return True