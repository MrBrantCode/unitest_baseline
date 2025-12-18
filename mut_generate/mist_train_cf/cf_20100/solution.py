"""
QUESTION:
Write a function named `calculate_trip_cost` that takes in three lists of equal length: `dates`, `hotel_costs`, and `quantities`. The function should calculate the total cost of a trip given the cost and quantity of hotel rooms, excluding weekends (Saturday and Sunday), and applying a 10% discount on weekend days. Additionally, the function should calculate the average cost per room for the entire trip, excluding weekends.
"""

from datetime import datetime

def calculate_trip_cost(dates, hotel_costs, quantities):
    """
    Calculate the total cost of a trip given the cost and quantity of hotel rooms, 
    excluding weekends (Saturday and Sunday), and applying a 10% discount on weekend days.
    
    Args:
        dates (list): A list of dates in the format 'YYYY-MM-DD'.
        hotel_costs (list): A list of hotel costs.
        quantities (list): A list of quantities of hotel rooms.
    
    Returns:
        tuple: A tuple containing the total cost of the trip and the average cost per room.
    """
    total_cost = 0
    total_rooms = 0
    
    for date, cost, quantity in zip(dates, hotel_costs, quantities):
        # Convert the date string to a datetime object
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        
        # Check if the date is a weekday (Monday to Friday)
        if date_obj.weekday() < 5:
            total_cost += cost * quantity
            total_rooms += quantity
        else:
            # Apply a 10% discount on weekends
            total_cost += cost * 0.9 * quantity
            total_rooms += quantity
    
    # Calculate the average cost per room
    if total_rooms > 0:
        average_cost = total_cost / total_rooms
    else:
        average_cost = 0
    
    return total_cost, average_cost