"""
QUESTION:
Write a function `analyze_sales_data` that takes a string parameter `file_path` representing the path to a CSV file containing sales data with columns 'ProductID', 'ProductName', 'Category', 'UnitPrice', 'Quantity', and 'TotalSales'. The function should return a dictionary with three keys: 'TotalSalesByCategory', 'TopSellingProducts', and 'OverallSalesStatistics'. The 'TotalSalesByCategory' value should be a pandas Series representing the total sales amount for each category. The 'TopSellingProducts' value should be a pandas DataFrame representing the top-selling product in each category. The 'OverallSalesStatistics' value should be a dictionary with keys 'TotalSalesAmount', 'AverageUnitPrice', and 'TotalQuantitySold' representing the overall sales statistics.
"""

import pandas as pd

def analyze_sales_data(file_path):
    # Read the CSV file into a pandas DataFrame
    sales_data = pd.read_csv(file_path)

    # Calculate the total sales amount for each category
    total_sales_by_category = sales_data.groupby('Category')['TotalSales'].sum()

    # Identify the top-selling product in each category
    top_selling_products = sales_data.loc[sales_data.groupby('Category')['TotalSales'].idxmax()]

    # Calculate the overall sales statistics
    overall_sales_statistics = {
        'TotalSalesAmount': sales_data['TotalSales'].sum(),
        'AverageUnitPrice': sales_data['UnitPrice'].mean(),
        'TotalQuantitySold': sales_data['Quantity'].sum()
    }

    return {
        'TotalSalesByCategory': total_sales_by_category,
        'TopSellingProducts': top_selling_products,
        'OverallSalesStatistics': overall_sales_statistics
    }