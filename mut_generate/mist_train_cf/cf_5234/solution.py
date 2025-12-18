"""
QUESTION:
Create a function called `average_summer_temperature` that calculates the average monthly temperature in Fahrenheit for June, July, and August. The function takes a list of 12 temperature readings, each representing a month of the year, as input. It should exclude any temperature readings below 80 degrees and above 90 degrees, and return the average temperature rounded to the nearest whole number.
"""

def average_summer_temperature(temperatures):
    summer_temperatures = temperatures[5:8]  # June, July, and August temperatures
    filtered_temperatures = [temp for temp in summer_temperatures if temp >= 80 and temp <= 90]
    return round(sum(filtered_temperatures) / len(filtered_temperatures))