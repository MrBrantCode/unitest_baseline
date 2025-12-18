"""
QUESTION:
Implement a function `calculate_average_true_range` that takes an array of integers `price_data` as input, representing high and low prices, and returns the average true range (ATR) rounded to 2 decimal places. The ATR is the average of the true range values over a specified period. The true range is the greatest of the difference between the current high and low, the absolute difference between the current high and the previous close, and the absolute difference between the current low and the previous close. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input array.
"""

def calculate_average_true_range(price_data):
    true_range_values = []
    
    for i in range(len(price_data)):
        if i == 0:
            true_range_values.append(abs(price_data[i][0] - price_data[i][1]))
        else:
            high_low_diff = abs(price_data[i][0] - price_data[i][1])
            high_prev_close_diff = abs(price_data[i][0] - price_data[i-1][1])
            low_prev_close_diff = abs(price_data[i][1] - price_data[i-1][1])
            
            true_range = max(high_low_diff, high_prev_close_diff, low_prev_close_diff)
            true_range_values.append(true_range)
    
    average_true_range = sum(true_range_values) / len(true_range_values)
    return round(average_true_range, 2)