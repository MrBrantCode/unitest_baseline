"""
QUESTION:
Create a function `distance_between` that calculates the total distance between a bus and a bicycle after a certain time. The function should take four parameters: the speed of the bus in km/h, the speed of the bicycle in km/h, the delay in minutes before the bicycle starts, and the total time in minutes. The bus and bicycle move in opposite directions. Return the total distance in kilometers.
"""

def distance_between(bus_speed, bike_speed, delay, total_time):
    bus_distance = bus_speed * total_time / 60
    bike_time = max(total_time - delay, 0)  # ensure bike_time is not negative
    bike_distance = bike_speed * bike_time / 60
    
    total_distance = bus_distance + bike_distance
    
    return total_distance