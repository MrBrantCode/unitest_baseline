"""
QUESTION:
Write a function `calculate_average_true_range` that takes a list of price data as input and returns the Average True Range (ATR) of the given price data, rounded to 1 decimal place. The ATR is calculated by taking the average of the True Range values over the given period. The True Range is the greatest of the difference between the current high and low, the absolute value of the difference between the current high and the previous close, and the absolute value of the difference between the current low and the previous close.
"""

def calculate_average_true_range(price_data):
    true_ranges = []
    
    for i in range(1, len(price_data)):
        high = price_data[i]
        low = price_data[i]
        previous_close = price_data[i - 1]
        
        true_range = max(high - low, abs(high - previous_close), abs(low - previous_close))
        true_ranges.append(true_range)
    
    average_true_range = sum(true_ranges) / len(true_ranges)
    return round(average_true_range, 1)