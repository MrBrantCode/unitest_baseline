"""
QUESTION:
Implement a function `find_cars_by_make_and_model` that takes in parameters `make`, `model`, `min_price`, `max_price`, `start_date`, and `end_date`. The function should return a list of cars that match the specified make, model, price range, and purchase date range. The function should filter the results from a given list of cars, where each car has attributes `make`, `model`, `price`, and `purchase_date`. The `start_date` and `end_date` parameters should be datetime objects.
"""

from datetime import datetime

def find_cars_by_make_and_model(cars, make, model, min_price, max_price, start_date, end_date):
    matching_cars = []
    for car in cars:
        if car.make == make and car.model == model and car.price >= min_price and car.price <= max_price and start_date <= car.purchase_date <= end_date:
            matching_cars.append(car)
    return matching_cars