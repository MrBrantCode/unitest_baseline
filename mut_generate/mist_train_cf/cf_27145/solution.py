"""
QUESTION:
Create a function `calculate_monthly_commuting_cost` that takes four parameters: `parking_pass_price_per_year` (annual cost of a parking pass), `drive_time_cost` (cost of driving per mile), `gas_cost` (cost of gas per gallon), and `days_on_campus_p_mo` (number of days commuting to campus per month). The function should calculate and return the total monthly commuting cost based on the given parameters.
"""

def calculate_monthly_commuting_cost(parking_pass_price_per_year, drive_time_cost, gas_cost, days_on_campus_p_mo):
    # Calculate the cost of a parking pass per month
    parking_pass_cost = parking_pass_price_per_year / 12

    # Calculate the total monthly commuting cost
    total_cost = (drive_time_cost + gas_cost) * days_on_campus_p_mo + parking_pass_cost
    return total_cost