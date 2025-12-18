"""
QUESTION:
Create a function named `calculate_co2_emissions` that takes two parameters: `mode_of_transportation` and `number_of_passengers`. The function should calculate and return the total CO2 emissions for a journey based on the given mode of transportation and number of passengers. The CO2 emissions per passenger for each mode of transportation are as follows:
- TGV: 0.009 kg/passenger
- Regional Train: 0.025 kg/passenger
- Bus: 0.040 kg/passenger
- Carpooling: 0.050 kg/passenger
- Car (gasoline): 0.120 kg/passenger
- Car (diesel): 0.140 kg/passenger
- Plane: 0.180 kg/passenger
If an invalid mode of transportation is entered, the function should return 0 and print an error message.
"""

def calculate_co2_emissions(mode_of_transportation, number_of_passengers):
    emissions_rates = {
        'TGV': 0.009,
        'Regional Train': 0.025,
        'Bus': 0.040,
        'Carpooling': 0.050,
        'Car (gasoline)': 0.120,
        'Car (diesel)': 0.140,
        'Plane': 0.180
    }
    
    if mode_of_transportation in emissions_rates:
        return emissions_rates[mode_of_transportation] * number_of_passengers
    else:
        print('Invalid mode of transportation')
        return 0