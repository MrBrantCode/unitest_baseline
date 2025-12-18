"""
QUESTION:
Map each XBRL position to one of the three financial statements: Balance Sheet, Income Statement, or Cash Flow Statement.

Create a function `map_xbrl_to_financial_statement` that takes an XBRL position as input and returns the corresponding financial statement. The function should be able to map XBRL positions to the following categories:
- Balance Sheet: Assets, Liabilities, and Shareholders' Equity
- Income Statement: Revenue, Cost of Goods Sold, Gross Profit, Operating Expenses, Operating Profit, Non-Operating Items, Pretax Profit, Tax, and Net Income
- Cash Flow Statement: Operating Activities, Investing Activities, and Financing Activities

The function should return one of the three financial statement names as a string.
"""

def map_xbrl_to_financial_statement(xbrl_position):
    """
    Maps an XBRL position to one of the three financial statements: Balance Sheet, Income Statement, or Cash Flow Statement.

    Args:
        xbrl_position (str): The XBRL position to be mapped.

    Returns:
        str: The corresponding financial statement.
    """

    # Define the XBRL positions for each financial statement
    balance_sheet_positions = ["Assets", "Liabilities", "Shareholders' Equity", "us-gaap:CashAndCashEquivalentsAtCarryingValue"]
    income_statement_positions = ["Revenue", "Cost of Goods Sold", "Gross Profit", "Operating Expenses", "Operating Profit", 
                                  "Non-Operating Items", "Pretax Profit", "Tax", "Net Income", "us-gaap:Revenues", 
                                  "us-gaap:IncomeTaxExpenseBenefit"]
    cash_flow_statement_positions = ["Operating Activities", "Investing Activities", "Financing Activities", 
                                     "us-gaap:CashProvidedByUsedInOperatingActivities"]

    # Check if the XBRL position belongs to the Balance Sheet
    if xbrl_position in balance_sheet_positions:
        return "Balance Sheet"
    
    # Check if the XBRL position belongs to the Income Statement
    elif xbrl_position in income_statement_positions:
        return "Income Statement"
    
    # Check if the XBRL position belongs to the Cash Flow Statement
    elif xbrl_position in cash_flow_statement_positions:
        return "Cash Flow Statement"
    
    # If the XBRL position does not match any of the above, return a message
    else:
        return "XBRL position not recognized"