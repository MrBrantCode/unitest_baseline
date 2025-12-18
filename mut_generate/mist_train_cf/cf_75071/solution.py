"""
QUESTION:
Write a function `max_wash_time` that calculates the maximum time in minutes a car can be washed at a self-service car wash station, given the total amount of money spent and the cost per quarter. The machine operates for 60 seconds per quarter. The function should take two parameters: `total_amount` (the total amount of money spent) and `cost_per_quarter` (the cost of one quarter). The function should return the maximum time in minutes the car can be washed. The total amount of money spent is $3.25 and the cost per quarter is $0.25.
"""

def max_wash_time(total_amount, cost_per_quarter):
    """
    Calculate the maximum time in minutes a car can be washed at a self-service car wash station.
    
    Parameters:
    total_amount (float): The total amount of money spent.
    cost_per_quarter (float): The cost of one quarter.
    
    Returns:
    float: The maximum time in minutes the car can be washed.
    """
    quarters = total_amount / cost_per_quarter
    total_time = quarters * 60  # each quarter operates the machine for 60 seconds
    total_time_in_minutes = total_time / 60  # convert total time from seconds to minutes
    return total_time_in_minutes