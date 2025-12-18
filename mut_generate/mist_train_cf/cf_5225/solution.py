"""
QUESTION:
Create a function called "car_to_dict" that takes a car object with attributes "make", "model", "year", "color", and "price" as a parameter and returns a dictionary representation of the car object. The dictionary should have the following key-value pairs: 
- "make" as the key for the car's make attribute value.
- "model" as the key for the car's model attribute value.
- "year" as the key for the car's year attribute value.
- "color" as the key for the car's color attribute value.
- "price" as the key for the car's price attribute value.

The function should handle any exceptions that may occur during the program execution. Implement error handling to handle any exceptions that may occur during the instantiation of the car objects and sorting of the list based on the "year" attribute.
"""

class Car:
    def __init__(self, make, model, year, color, price):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.price = price

def car_to_dict(car):
    """
    This function takes a car object as a parameter and returns a dictionary representation of the car object.
    
    Args:
        car (Car): A car object with attributes "make", "model", "year", "color", and "price".
    
    Returns:
        dict: A dictionary representation of the car object.
    """
    try:
        return {
            "make": car.make,
            "model": car.model,
            "year": car.year,
            "color": car.color,
            "price": car.price
        }
    except Exception as e:
        raise Exception("An error occurred while converting the car object to a dictionary: " + str(e))