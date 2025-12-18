"""
QUESTION:
Develop a function named `get_city_revenue(city_name)` that checks if a given city name exists in a predefined table and if revenue data is available for that city. If the city name is found, return the total revenue for that city in AUD. If the city name is not found, return an error message. If the city name is found but revenue data is not available, return a message indicating that revenue data is not available for that city. The function should utilize a series of nested if-else statements and should compare the input with every city in the table.
"""

def get_city_revenue(city_name):
    # define the table
    table = [
        {"city": "Sydney", "revenue": 100000},
        {"city": "Melbourne", "revenue": 90000},
        {"city": "Brisbane", "revenue": 75000},
        {"city": "Perth", "revenue": 60000},
        {"city": "Adelaide", "revenue": 45000}
    ]
    
    # check if city_name is in the table
    if city_name in [city['city'] for city in table]:
        # city_name is in the table, check if revenue is available
        for city in table:
            if city['city'] == city_name:
                # revenue is available for the city
                return "The total revenue for {} is {} AUD".format(city_name, city['revenue'])
        # revenue is not available for the city
        return "Revenue data is not available for {}".format(city_name)
    # city_name is not in the table
    else:
        return "{} is not a valid city name".format(city_name)