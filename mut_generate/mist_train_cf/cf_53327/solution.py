"""
QUESTION:
Write a Python function `manipulate_data` that takes in a list of data and returns the cleaned data. The data may contain various issues such as missing or inconsistent data, incorrect formatting, and redundancy. The function should handle these issues, ensure data uniformity, and minimize impact on data flow rate.
"""

def manipulate_data(data):
    """
    This function takes in a list of data, handles issues such as missing or inconsistent data, 
    incorrect formatting, and redundancy, ensures data uniformity, and minimizes impact on data flow rate.

    Args:
        data (list): The input data that needs to be cleaned.

    Returns:
        list: The cleaned data.
    """
    # Format parsing
    parsed_data = [item.strip() for item in data if item]

    # Consistent schemas
    consistent_data = [item for item in parsed_data if len(item.split(',')) == 2]

    # Data cleaning
    cleaned_data = []
    for item in consistent_data:
        try:
            key, value = item.split(',')
            if key and value:
                cleaned_data.append((key, value))
        except ValueError:
            pass

    return cleaned_data