"""
QUESTION:
Write a function called `calculate_average_true_range` that takes an array of price data as input and returns the average true range as a float rounded to 1 decimal place. The function should calculate the true range for each price in the array using the formula: the greatest of the difference between the current high and low, the absolute difference between the current high and previous close, and the absolute difference between the current low and previous close.
"""

def calculate_average_true_range(price_data):
    true_ranges = []
    
    for i in range(1, len(price_data)):
        high = max(price_data[i][1], price_data[i][2])
        low = min(price_data[i][1], price_data[i][2])
        previous_close = price_data[i - 1][4]
        
        true_range = max(high - low, abs(high - previous_close), abs(low - previous_close))
        true_ranges.append(true_range)
    
    average_true_range = sum(true_ranges) / len(true_ranges)
    return round(average_true_range, 1)