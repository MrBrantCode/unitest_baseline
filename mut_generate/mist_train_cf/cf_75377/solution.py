"""
QUESTION:
Calculate the average speeds and time taken for a truck's round trip from point C to D and back. The truck travels at varying speeds on the way to D, and its speed is reduced by 20% on the return journey due to added cargo. However, the truck's speed on the return journey is 10% faster than its average speed on the way to D. 

The function `truck_journey` should take four parameters: distance (in km), onward_time (in minutes), cargo_weight (in kg), and repair_time (in minutes). It should calculate the average speed for the onward journey, return journey, and entire round trip (in km/hr), as well as the time taken for both journeys (in minutes). The function should account for the added weight of the cargo and any repair time during the return journey.
"""

def truck_journey(distance, onward_time, cargo_weight, repair_time):
    # Calculate average speed for the onward journey in km/hr
    onward_speed = distance / (onward_time / 60)

    # Calculate average speed for the return journey
    # Speed is reduced by 20% due to cargo, then increased by 10% of the average speed on the way to D
    return_speed = 0.8 * onward_speed + 0.1 * onward_speed

    # Calculate time taken for the return journey taking into account the repair time
    return_time = (distance / return_speed * 60) + repair_time

    # Calculate average speed for the entire round trip
    total_time = onward_time + return_time
    total_speed = 2 * distance / (total_time / 60)

    return {
        'onward_speed': round(onward_speed, 2),
        'return_speed': round(return_speed, 2),
        'total_speed': round(total_speed, 2),
        'onward_time': round(onward_time, 2),
        'return_time': round(return_time, 2)
    }