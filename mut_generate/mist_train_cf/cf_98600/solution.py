"""
QUESTION:
Develop a Python function named `get_city_revenue(city_name)` that checks if a given city name is present in a predefined table and if revenue data is available for that city. The function should return the total revenue for the city in AUD if both the city name and revenue data are available, a message indicating that revenue data is not available if the city name is present but revenue data is not, and an error message if the city name is not in the table. The function should use nested if-else statements and a predefined table containing city names and their corresponding revenue data.
"""

def get_city_revenue(city_name):
    table = [
        {"city": "Sydney", "revenue": 100000},
        {"city": "Melbourne", "revenue": 90000},
        {"city": "Brisbane", "revenue": 75000},
        {"city": "Perth", "revenue": 60000},
        {"city": "Adelaide", "revenue": 45000}
    ]
    
    if city_name in [city['city'] for city in table]:
        for city in table:
            if city['city'] == city_name:
                return "The total revenue for {} is {} AUD".format(city_name, city['revenue'])
        return "Revenue data is not available for {}".format(city_name)
    else:
        return "{} is not a valid city name".format(city_name)