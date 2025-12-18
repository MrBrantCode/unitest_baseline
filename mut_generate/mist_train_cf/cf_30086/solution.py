"""
QUESTION:
Create a function called `format_sensor_readings` that takes UV index, visible light, infrared light, temperature, and humidity values as input and returns a string that formats these readings in the following format:
```
UV_index:<UV_index_value>
Visible:<visible_light_value>
IR:<infrared_value>
======== bme280 ========
temperature:<temperature_value>
humidity:<humidity_value>
```
Where `<UV_index_value>` and `<temperature_value>` are rounded to two decimal places, and `<visible_light_value>`, `<infrared_value>`, and `<humidity_value>` are integers.
"""

def format_sensor_readings(UV_index, visible_light, infrared, temperature, humidity):
    """
    Formats the sensor readings into a string.

    Args:
        UV_index (float): The UV index reading.
        visible_light (int): The visible light reading.
        infrared (int): The infrared light reading.
        temperature (float): The temperature reading.
        humidity (float): The humidity reading.

    Returns:
        str: A formatted string containing the sensor readings.
    """
    return (
        f"UV_index:{UV_index:.2f}\n"
        f"Visible:{visible_light}\n"
        f"IR:{infrared}\n"
        "======== bme280 ========\n"
        f"temperature:{temperature:.2f}\n"
        f"humidity:{humidity:.0f}"
    )