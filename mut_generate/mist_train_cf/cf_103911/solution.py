"""
QUESTION:
Create a function `get_num_cities` that takes a country name as input and returns the number of cities in that country. The function must have a time complexity of O(1). The function should return 0 if the country name is not found.
"""

countries = {
    "USA": ["New York", "Los Angeles", "Chicago"],
    "India": ["Mumbai", "Delhi", "Bangalore"],
    "Japan": ["Tokyo", "Osaka"],
    "Germany": ["Berlin", "Munich"]
}

def get_num_cities(country):
    if country in countries:
        return len(countries[country])
    else:
        return 0