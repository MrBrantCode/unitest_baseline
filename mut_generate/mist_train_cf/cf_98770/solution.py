"""
QUESTION:
Write a function `calculate_carbon_footprint` that takes four parameters: the number of people in a household (`num_people`), monthly electricity consumption in kilowatt-hours (`electricity_consumption`), monthly gas consumption in therms (`gas_consumption`), and monthly mileage of vehicles (`mileage`). The function should return the total carbon footprint of the household in metric tons of CO2 emissions.
"""

def calculate_carbon_footprint(num_people, electricity_consumption, gas_consumption, mileage):
    # Constants for carbon emissions per unit of energy
    ELECTRICITY_EMISSIONS = 0.0005 # metric tons CO2 per kWh
    GAS_EMISSIONS = 0.0053 # metric tons CO2 per therm
    VEHICLE_EMISSIONS = 0.00012 # metric tons CO2 per mile
    
    # Calculate carbon emissions from electricity and gas consumption
    electricity_emissions = ELECTRICITY_EMISSIONS * electricity_consumption
    gas_emissions = GAS_EMISSIONS * gas_consumption
    
    # Calculate carbon emissions from vehicle mileage
    vehicle_emissions = VEHICLE_EMISSIONS * mileage
    
    # Calculate total carbon footprint
    total_emissions = (electricity_emissions + gas_emissions + vehicle_emissions) * 12 * num_people
    
    # Convert to metric tons
    total_emissions = total_emissions / 1000
    
    return total_emissions