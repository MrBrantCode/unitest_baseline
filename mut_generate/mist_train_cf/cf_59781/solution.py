"""
QUESTION:
Write a function `calculate_distance` that calculates how far apart a bus and a bicycle are after a given amount of time. The bus travels at a certain speed, stops intermittently, and its stops are not fixed and can last different amounts of time. The bicycle travels at a different speed. The function should take the bus speed, the bus stops (as a list of tuples containing stop times and durations), the bicycle speed, and the time they are both in motion as input. The function should return the absolute difference between the distances travelled by the bike and the bus.
"""

def calculate_distance(bus_speed, bus_stops, bike_speed, time_in_motion):
    t_motion_adjusted = time_in_motion
    for stop in bus_stops:
        if stop[0] < time_in_motion:
            t_motion_adjusted -= stop[1]
    bus_distance = bus_speed * t_motion_adjusted
    bike_distance = bike_speed * time_in_motion
    return abs(bus_distance - bike_distance)