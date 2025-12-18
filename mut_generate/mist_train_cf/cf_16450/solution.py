"""
QUESTION:
Calculate the average true range of a given array of price data. The true range for each price is the greatest of the absolute difference between the current high and low, the absolute difference between the current high and the previous close, and the absolute difference between the current low and the previous close. The average true range is the average of all true range values.

The function `calculate_average_true_range` should take an array `price_data` as input, where `price_data[i]` represents the price at time `i`. The function should return the calculated average true range rounded to 2 decimal places.

Constraints: The length of `price_data` is at most 10^5 and the values in `price_data` are integers in the range [-10^9, 10^9].
"""

def calculate_average_true_range(price_data):
    true_range_values = []
    for i in range(1, len(price_data)):
        current_high = price_data[i]
        current_low = price_data[i]
        previous_close = price_data[i-1]
        
        true_range = max(current_high - current_low, abs(current_high - previous_close), abs(current_low - previous_close))
        true_range_values.append(true_range)
    
    average_true_range = sum(true_range_values) / len(true_range_values)
    return round(average_true_range, 2)