"""
QUESTION:
Write a function `calculate_carbon_footprint(num_people, electricity_consumption, gas_consumption, mileage)` to calculate the total carbon footprint of a household in metric tons of CO2 emissions. The function should take in the following inputs: `num_people`, the number of people in the household; `electricity_consumption`, the monthly electricity consumption in kilowatt-hours (kWh); `gas_consumption`, the monthly gas consumption in therms; and `mileage`, the monthly mileage of any vehicles in the household. Assume the following constants for carbon emissions per unit of energy: 0.0005 metric tons CO2 per kWh for electricity, 0.0053 metric tons CO2 per therm for gas, and 0.00012 metric tons CO2 per mile for vehicle mileage.
"""

def calculate_carbon_footprint(num_people, electricity_consumption, gas_consumption, mileage):
    # Constants for carbon emissions per unit of energy
    ELECTRICITY_EMISSIONS = 0.0005  # metric tons CO2 per kWh
    GAS_EMISSIONS = 0.0053  # metric tons CO2 per therm
    VEHICLE_EMISSIONS = 0.00012  # metric tons CO2 per mile

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