"""
QUESTION:
Create a function `calculate_ride_cost` that takes four arguments: `distance` (float, distance in miles), `duration` (int, duration of the ride in minutes), `start_time` (string, time the ride started in a 24-hour format, e.g. "08:30"), and `vehicle_type` (string, either "standard" or "luxury"). 

The function should return the total cost of the ride, calculated as follows: basic cost ($0.005 per minute per mile) plus a 15% increase if the ride is during rush hour (7am-10am and 4pm-8pm), a 20% surcharge if the vehicle is luxury, and a 7.5% tax, all rounded up to the nearest integer.
"""

def calculate_ride_cost(distance, duration, start_time, vehicle_type):
    # Compute the basic cost
    basic_cost = 0.005 * duration * distance
    
    # Apply rush hour pricing if applicable
    hour = int(start_time.split(':')[0])
    if (7 <= hour <= 10) or (16 <= hour <= 20):
        basic_cost *= 1.15
    
    # Apply luxury surcharge if applicable
    if vehicle_type == 'luxury':
        basic_cost *= 1.20
    
    # Compute the total cost
    total_cost = basic_cost * 1.075  # add 7.5% tax
    
    # Round up to the nearest integer
    total_cost = round(total_cost + 0.4999)
    
    return total_cost