"""
QUESTION:
Write a function named `average_speed` that takes two lists, `distances` and `speeds`, as inputs and returns the average speed of the bus for the entire trip. The lists `distances` and `speeds` have equal length and represent the distances traveled and the corresponding speeds in kilometers and kilometers per hour, respectively. The function should calculate the average speed as the total distance traveled divided by the total time spent traveling, round the result to two decimal places, and return it.
"""

def average_speed(distances, speeds):
    # Using zip function to pair each distance value with its corresponding speed value
    # Calculating time for each part of the trip by dividing distance by speed
    times = [d/s for d, s in zip(distances, speeds)]
    
    # Calculating total distance (sum of all distances) and total time (sum of all times)
    total_distance = sum(distances)
    total_time = sum(times)
    
    # Calculating average speed (total distance / total time)
    avg_speed = total_distance / total_time

    return round(avg_speed, 2)  # Rounding off to two decimal places before returning