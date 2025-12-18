"""
QUESTION:
Create a function `create_pivot_table` that takes a pandas DataFrame `df` as input, where the DataFrame has columns 'product_name' and 'quantity'. The function should return a new DataFrame where the index is each unique value in the 'product_name' column and the value is the sum of the 'quantity' for that product. The function should display the total quantity sold for every unique product in the DataFrame.
"""

def create_pivot_table(df):
    return df.pivot_table(values='quantity', index='product_name', aggfunc='sum')