"""
QUESTION:
Write a function named `calculate_months_to_save` that takes the initial values of the current car, new car, monthly savings, initial depreciation rate, and depreciation rate increase as parameters. The function should return the number of months it will take to save up enough money to buy the new car and the remaining money after the purchase. The current car value and new car value decrease by the depreciation rate every month, and the depreciation rate increases by the depreciation rate increase every month.
"""

def calculate_months_to_save(current_car_value, new_car_value, monthly_savings, initial_depreciation_rate, depreciation_rate_increase):
    months = 0
    depreciation_rate = initial_depreciation_rate
    current_value = current_car_value
    while current_value < new_car_value:
        # calculate the value of both cars after depreciation
        current_value += monthly_savings
        current_value -= current_value * depreciation_rate
        new_car_value -= new_car_value * depreciation_rate
        depreciation_rate += depreciation_rate_increase
        months += 1
    # calculate how much money is left after the purchase
    remaining_money = current_value - new_car_value
    return months, remaining_money