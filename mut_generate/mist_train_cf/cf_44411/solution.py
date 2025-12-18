"""
QUESTION:
Create a function named `average_speed` that takes two lists of speeds `to_destination` and `from_destination` as input and returns the car's average speed for the entire round trip. The function should assume that the car travels 1 unit of distance at each speed in both lists, and calculate the average speed by dividing the total distance by the total time taken. The function should return the average speed in miles per hour, rounded to one decimal place.
"""

def average_speed(to_destination, from_destination):
    total_distance = 0.0
    total_time = 0.0
    for i in range(len(to_destination)):
        total_distance += 1 
        total_time += 1/to_destination[i]
        total_time += 1/from_destination[i]
    average_speed = total_distance/total_time
    return round(average_speed, 1)