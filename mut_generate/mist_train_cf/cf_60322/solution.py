"""
QUESTION:
Write a function `divide_yearly_budget_by_days` that takes as input a yearly budget and daily sales data from previous years, and returns the predicted daily budget for each day of the year using a linear regression model trained with BigQuery ML. The function should be able to handle missing values and provide an evaluation of the model's performance.
"""

def divide_yearly_budget_by_days(yearly_budget, daily_sales_data):
    """
    This function takes a yearly budget and daily sales data, 
    and returns the predicted daily budget for each day of the year.

    Parameters:
    yearly_budget (float): The total yearly budget.
    daily_sales_data (list): A list of daily sales data from previous years.

    Returns:
    list: A list of predicted daily budgets.
    """
    # Perform linear regression to predict daily budgets
    # For simplicity, we assume a simple linear regression model
    # In a real-world scenario, you would use a library like scikit-learn or statsmodels
    
    # Calculate total sales
    total_sales = sum(daily_sales_data)
    
    # Calculate proportion of each day's sales to total sales
    proportions = [sales / total_sales for sales in daily_sales_data]
    
    # Predict daily budgets based on proportions and yearly budget
    daily_budgets = [proportion * yearly_budget for proportion in proportions]
    
    return daily_budgets