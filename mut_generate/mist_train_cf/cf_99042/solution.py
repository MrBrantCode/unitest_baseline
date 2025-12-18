"""
QUESTION:
Write a function `calculate_sector_trends` that calculates the mean and median of stock prices for each sector, determines the trend based on the mean and median values, and returns the results. The function should take a list of sector names and a list of corresponding lists of stock prices as input. The trend should be determined as upward if the mean is greater than the median, downward if the mean is less than the median, and stable if the mean and median are equal. The function should return a dictionary where the keys are sector names and the values are dictionaries with 'mean', 'median', and 'trend' as keys.
"""

import statistics

def calculate_sector_trends(sectors, prices):
    trends = {}
    
    for sector, price_list in zip(sectors, prices):
        mean = sum(price_list) / len(price_list)
        median = statistics.median(price_list)
        
        if mean > median:
            trend = "upward"
        elif mean < median:
            trend = "downward"
        else:
            trend = "stable"
        
        trends[sector] = {
            'mean': mean,
            'median': median,
            'trend': trend
        }
    
    return trends