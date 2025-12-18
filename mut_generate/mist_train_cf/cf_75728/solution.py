"""
QUESTION:
Write a function called `convert_temp` that takes an array of temperature values in Fahrenheit as strings (e.g., "56.4F") and returns a list of tuples, each containing the corresponding temperature in Celsius and Kelvin. The function should handle potential erroneous input data, reporting any invalid inputs and continuing with the next value.
"""

def convert_temp(temps):
    """Convert an array of temperatures from Fahrenheit to Celsius and Kelvin"""
    results = []
    for temp in temps:
        try:
            f = float(temp[:-1])  # Ignore the trailing 'F'
            c = (f - 32) * (5/9)
            k = c + 273.15
            results.append((c, k))
        except ValueError:
            print("Invalid input: '{}'".format(temp))
        except Exception as e:
            print("An unexpected error occurred: {}".format(e))
    return results