"""
QUESTION:
Write a function `incremental_refresh` that takes in a list of monthly data and returns the combined data without overwriting previous months' data. The function should allow incremental updates to the data without requiring a full refresh.
"""

def incremental_refresh(monthly_data):
    """
    This function combines monthly data without overwriting previous months' data.
    
    Args:
        monthly_data (list): A list of lists containing monthly data.
        
    Returns:
        list: The combined data.
    """
    # Initialize an empty list to store the combined data
    combined_data = []
    
    # Iterate over each month's data
    for month in monthly_data:
        # Extend the combined data with the current month's data
        combined_data.extend(month)
    
    # Return the combined data
    return combined_data