"""
QUESTION:
Create a function named `create_hierarchical_dataframe` that takes in a pandas DataFrame with columns 'Region', 'Name', and 'Sales' as input, groups the data by 'Region' and 'Name', and returns a hierarchical DataFrame with 'Sales' aggregated by 'mean', 'median', and 'sum'.
"""

def create_hierarchical_dataframe(df):
    """
    Creates a hierarchical DataFrame by grouping the input DataFrame by 'Region' and 'Name', 
    and aggregating 'Sales' by 'mean', 'median', and 'sum'.

    Args:
        df (pd.DataFrame): Input DataFrame with columns 'Region', 'Name', and 'Sales'.

    Returns:
        pd.DataFrame: Hierarchical DataFrame with 'Sales' aggregated by 'mean', 'median', and 'sum'.
    """
    # Group by Region and Name
    grouped = df.groupby(['Region', 'Name'])
    
    # Perform aggregation operations on the grouped data
    aggregated = grouped.agg({"Sales": ['mean', 'median', 'sum']})
    
    return aggregated