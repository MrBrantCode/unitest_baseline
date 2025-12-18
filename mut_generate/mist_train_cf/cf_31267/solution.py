"""
QUESTION:
Write a function `extract_car_info` that takes a JSON object as input and extracts the following information:
- Car number
- Car name
- Manufacturer
- Fuel type
- Safety options
- Convenience options

The function should return the extracted information in a readable format. The JSON object contains various attributes about a car model, including "number", "name", "manufacturer", "fuel_type", "safety_option", and "convenience_option". The safety options and convenience options are comma-separated strings that need to be split into lists.
"""

def extract_car_info(car_json):
    """
    Extracts car information from a given JSON object.

    Args:
        car_json (dict): A dictionary containing car attributes.

    Returns:
        dict: A dictionary containing the extracted car information.
    """
    car_info = {
        "Car Number": car_json["number"],
        "Car Name": car_json["name"],
        "Manufacturer": car_json["manufacturer"],
        "Fuel Type": car_json["fuel_type"],
        "Safety Options": car_json["safety_option"].split(", "),
        "Convenience Options": car_json["convenience_option"].split(", ")
    }

    return car_info