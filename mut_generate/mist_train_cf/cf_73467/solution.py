"""
QUESTION:
Create a function `calculate_insurance_price` that takes three parameters: `age`, `gender`, and `car_model`. The function should calculate a hypothetical insurance price based on the given parameters. If the age is less than 25, add $500 to the base price of $1000. If the gender is 'male', add $200 to the price. If the car model is 'sports', add $300 to the price. Return the calculated insurance price.
"""

def calculate_insurance_price(age, gender, car_model):
    price = 1000
    if int(age) < 25:
        price += 500
    if gender.lower() == 'male':
        price += 200
    if car_model.lower() == 'sports':
        price += 300
    return price