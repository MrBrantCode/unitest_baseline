"""
QUESTION:
Estimate DW's 2020 earnings given its 2019 performance. The function should be named `estimate_2020_earnings`. DW's performance is defined by the following parameters: 

- D/E ratio is 0.5
- ROE is 0.1
- Sales per dollar in assets is $0.2
- Average accounts receivables is $2 million 

Assuming DW's performance remains consistent from 2019 to 2020, return an estimate of its 2020 earnings in dollars.
"""

def estimate_2020_earnings(debt_to_equity_ratio, return_on_equity, sales_per_dollar_in_assets, average_accounts_receivables):
    """
    Estimates DW's 2020 earnings based on its 2019 performance.

    Args:
    debt_to_equity_ratio (float): D/E ratio
    return_on_equity (float): ROE
    sales_per_dollar_in_assets (float): Sales per dollar in assets
    average_accounts_receivables (float): Average accounts receivables

    Returns:
    float: Estimated 2020 earnings
    """
    # Calculate total assets
    total_assets = average_accounts_receivables / sales_per_dollar_in_assets
    
    # Calculate shareholder's equity
    shareholders_equity = total_assets / (1 + debt_to_equity_ratio)
    
    # Calculate net income (earnings)
    net_income = return_on_equity * shareholders_equity
    
    return net_income