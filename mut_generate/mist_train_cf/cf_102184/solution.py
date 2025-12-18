"""
QUESTION:
Write a function `convert_distance_to_kilometers` that takes in two parameters: `distance` (in miles) and `time` (in minutes). The function should convert the distance from miles to kilometers, calculate the speed in kilometers per hour, and return the speed. The function should also handle any potential errors or edge cases that may occur during the conversion or calculation. The function should return `None` in case of an error.
"""

def convert_distance_to_kilometers(distance, time):
    try:
        distance_km = distance * 1.60934  # Conversion factor from miles to kilometers
        time_hr = time / 60  # Conversion factor from minutes to hours
        speed = distance_km / time_hr
        return speed
    except Exception as e:
        print("Error occurred:", e)
        return None