"""
QUESTION:
Create a Python function `flag_sensor_limits` that takes a `datetime` array and a variable number of sensor readings arrays as input. The function should identify and flag any instances where the sensor readings exceed predefined limits, which are as follows: 
- `Shroud1` and `Shroud2`: 100
- `channel_11`, `channel_12`, and `channel_13`: 50
- `channel_26`, `channel_27`, and `channel_28`: 200 
The function should return a list of timestamps where the sensor readings exceed the limits.
"""

def flag_sensor_limits(datetime, *sensor_readings):
    flagged_timestamps = []
    limits = {'Shroud1': 100, 'Shroud2': 100, 'channel_11': 50, 'channel_12': 50, 'channel_13': 50,
              'channel_26': 200, 'channel_27': 200, 'channel_28': 200}

    for i in range(len(datetime)):
        for j, (sensor, reading) in enumerate(zip(sensor_readings[::2], sensor_readings[1::2])):
            if reading[i] > limits.get(sensor, float('inf')):
                flagged_timestamps.append(datetime[i])
                break  # Move to the next timestamp

    return flagged_timestamps