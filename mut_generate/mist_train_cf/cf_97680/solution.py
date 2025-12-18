"""
QUESTION:
Write a function named `calculate_carbon_footprint` that takes four parameters: `num_people`, `electricity_consumption` (in kWh), `gas_consumption` (in therms), and `mileage`. The function should return the total carbon footprint of a household in metric tons of CO2 emissions. The carbon emissions per unit of energy are: 0.0005 metric tons CO2 per kWh of electricity, 0.0053 metric tons CO2 per therm of gas, and 0.00012 metric tons CO2 per mile of vehicle mileage.
"""

def calculate_carbon_footprint(num_people, electricity_consumption, gas_consumption, mileage):
    ELECTRICITY_EMISSIONS = 0.0005  # metric tons CO2 per kWh
    GAS_EMISSIONS = 0.0053  # metric tons CO2 per therm
    VEHICLE_EMISSIONS = 0.00012  # metric tons CO2 per mile

    electricity_emissions = ELECTRICITY_EMISSIONS * electricity_consumption
    gas_emissions = GAS_EMISSIONS * gas_consumption
    vehicle_emissions = VEHICLE_EMISSIONS * mileage

    total_emissions = (electricity_emissions + gas_emissions + vehicle_emissions) * 12 * num_people
    total_emissions = total_emissions / 1000

    return total_emissions