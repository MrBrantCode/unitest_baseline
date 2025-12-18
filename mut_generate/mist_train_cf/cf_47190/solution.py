"""
QUESTION:
Create a function named `calculate_data_skew` that takes a dictionary where keys are country codes and values are the frequency of website logs from each country. The function should calculate and return the data skew ratio.

The data skew ratio is calculated as the maximum frequency divided by the average frequency of all country codes. The input dictionary is expected to have at least two country codes.
"""

def calculate_data_skew(country_freq):
    """
    Calculate the data skew ratio from a dictionary of country codes and their frequencies.

    Args:
    country_freq (dict): A dictionary where keys are country codes and values are the frequency of website logs from each country.

    Returns:
    float: The data skew ratio calculated as the maximum frequency divided by the average frequency of all country codes.
    """
    
    # Calculate the total frequency
    total_freq = sum(country_freq.values())
    
    # Calculate the average frequency
    avg_freq = total_freq / len(country_freq)
    
    # Calculate the maximum frequency
    max_freq = max(country_freq.values())
    
    # Calculate the data skew ratio
    data_skew_ratio = max_freq / avg_freq
    
    return data_skew_ratio