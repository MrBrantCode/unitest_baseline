"""
QUESTION:
Create a function `calculate_travel_time` that calculates the estimated travel time for a car to travel a given distance. The car's speed is calculated as 60 km / 45 minutes. The function should take a distance in kilometers as input and return the travel time in hours, minutes, and seconds. Ensure the input distance is a positive number and return an error message if it is not.
"""

def calculate_travel_time(distance):
    # Error checking to ensure that the distance is a positive number.
    if distance<0:
        return "Error! Distance cannot be negative."
    # Speed = Distance/Time
    # Calculate speed in km/minute
    speed = 60/45
    # Time = Distance/Speed
    # Calculate time taken to travel in minutes
    travel_time = distance/speed
    # Convert the time from minutes to hours and seconds
    hours = int(travel_time // 60)
    minutes = int(travel_time % 60)
    seconds = int((travel_time % 1) * 60)
    return f"Estimated travel time is: {hours} hours, {minutes} minutes, and {seconds} seconds."