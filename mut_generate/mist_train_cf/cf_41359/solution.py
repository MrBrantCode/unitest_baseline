"""
QUESTION:
Create a function `calculate_fuel_efficiency` that takes seven parameters: `bore` (float), `stroke` (float), `compression_ratio` (float), `horsepower` (float), `peak_rpm` (int), `city_mpg` (int), and `highway_mpg` (int). The function should calculate the fuel efficiency using the formula: `(2 * bore * stroke * compression_ratio * horsepower / peak_rpm) + (city_mpg + highway_mpg) / 2`, and return the result rounded to two decimal places.
"""

def calculate_fuel_efficiency(bore, stroke, compression_ratio, horsepower, peak_rpm, city_mpg, highway_mpg):
    fuel_efficiency = (2 * bore * stroke * compression_ratio * horsepower / peak_rpm) + (city_mpg + highway_mpg) / 2
    return round(fuel_efficiency, 2)