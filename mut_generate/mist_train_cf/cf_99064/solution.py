"""
QUESTION:
Write a function `calculate_co2_emissions(mode_of_transportation, number_of_passengers)` that takes two arguments: the mode of transportation and the number of passengers. The function should calculate and return the total CO2 emissions based on the mode of transportation selected from the given table:
| Mode of Transportation | CO2 Emissions (kg/passenger) |
|------------------------|-------------------------------|
| TGV                    | 0.009                         |
| Regional Train         | 0.025                         |
| Bus                    | 0.040                         |
| Carpooling             | 0.050                         |
| Car (gasoline)         | 0.120                         |
| Car (diesel)           | 0.140                         |
| Plane                  | 0.180                         |
If an invalid mode of transportation is entered, the function should return 0 and print an error message.
"""

def calculate_co2_emissions(mode_of_transportation, number_of_passengers):
    if mode_of_transportation == 'TGV':
        co2_emissions = 0.009 * number_of_passengers
    elif mode_of_transportation == 'Regional Train':
        co2_emissions = 0.025 * number_of_passengers
    elif mode_of_transportation == 'Bus':
        co2_emissions = 0.040 * number_of_passengers
    elif mode_of_transportation == 'Carpooling':
        co2_emissions = 0.050 * number_of_passengers
    elif mode_of_transportation == 'Car (gasoline)':
        co2_emissions = 0.120 * number_of_passengers
    elif mode_of_transportation == 'Car (diesel)':
        co2_emissions = 0.140 * number_of_passengers
    elif mode_of_transportation == 'Plane':
        co2_emissions = 0.180 * number_of_passengers
    else:
        co2_emissions = 0
        print('Invalid mode of transportation')
    return co2_emissions