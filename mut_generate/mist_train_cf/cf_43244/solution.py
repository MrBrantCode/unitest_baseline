"""
QUESTION:
Implement a function `change_lane` inside the `process_function` method of the `TrafficSystem` class. The function `change_lane` should take a dictionary `data` representing the current state of the traffic system, with the following structure:
- `data` contains two keys: `status` and `drive`.
- `data['status']` contains a key `car` with keys `position` and `speed`.
- `data['drive']` contains a key `lanes` representing the number of lanes on the road.

The `change_lane` function should change the lane of a car based on the following conditions:
- If the car's speed is greater than 80, it should move to the left lane if available.
- If the car's speed is less than 40, it should move to the right lane if available.
- If the car's speed is between 40 and 80 (inclusive), it should stay in the current lane.
"""

def change_lane(data):
    """
    Changes the lane of a car based on its speed and current position.

    Args:
    data (dict): A dictionary representing the current state of the traffic system.

    Returns:
    dict: The updated data dictionary with the car's new position.
    """
    car = data['status']['car']
    drive = data['drive']

    if car['speed'] > 80 and car['position'] > 0:
        car['position'] -= 1  # Move to the left lane
    elif car['speed'] < 40 and car['position'] < drive['lanes'] - 1:
        car['position'] += 1  # Move to the right lane

    return data  # Return the updated data