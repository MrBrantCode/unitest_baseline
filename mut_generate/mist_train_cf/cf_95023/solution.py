"""
QUESTION:
Create a function `miles_to_kilometers(distance, time)` that takes two parameters, `distance` in miles and `time` in hours, and returns a tuple containing the distance in kilometers and the speed in kilometers per hour. The function should handle cases where `distance` or `time` are non-numeric, where `time` is zero, and any other unexpected errors.
"""

def miles_to_kilometers(distance, time):
    try:
        # Convert distance from miles to kilometers
        kilometers = distance * 1.60934

        # Calculate speed in kilometers per hour
        speed = kilometers / time

        return kilometers, speed

    except TypeError:
        return "Error: Distance and time must be numeric values."

    except ZeroDivisionError:
        return "Error: Time cannot be zero."

    except Exception as e:
        return "An error occurred: " + str(e)