"""
QUESTION:
Find the names of the top 10 cities with the highest population within a specified distance from a given set of coordinates. The function `find_top_cities` should take in the city data, the center coordinates, the distance, and the number of top cities to find. It should return a list of dictionaries containing the city information.

Additionally, calculate and print the average population density within the specified distance from the given coordinates. The function `calculate_average_density` should take in the city data, the center coordinates, and the distance. It should return the average population density.

Constraints:
- The city data may contain millions of entries.
- The functions should have a time complexity of O(nlogn) or better.
- The functions should have a space complexity of O(1) or better. 

The city data is a list of dictionaries where each dictionary contains the city's name, population, latitude, and longitude. The coordinates are in decimal degrees. The distance is in kilometers. The Earth is assumed to be a perfect sphere, and the haversine formula is used to calculate the distance between two sets of coordinates.
"""

import math

def find_top_cities(city_data, center_lat, center_lon, distance, num_cities):
    def haversine_distance(lat1, lon1, lat2, lon2):
        # Radius of the Earth in kilometers
        R = 6371.0

        # Convert coordinates to radians
        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)
        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)

        # Haversine formula
        dlon = lon2_rad - lon1_rad
        dlat = lat2_rad - lat1_rad
        a = math.sin(dlat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        distance = R * c

        return distance

    filtered_cities = [city for city in city_data if haversine_distance(center_lat, center_lon, city['latitude'], city['longitude']) <= distance]
    sorted_cities = sorted(filtered_cities, key=lambda city: city['population'], reverse=True)
    top_cities = sorted_cities[:num_cities]

    return top_cities

def calculate_average_density(city_data, center_lat, center_lon, distance):
    def haversine_distance(lat1, lon1, lat2, lon2):
        # Radius of the Earth in kilometers
        R = 6371.0

        # Convert coordinates to radians
        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)
        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)

        # Haversine formula
        dlon = lon2_rad - lon1_rad
        dlat = lat2_rad - lat1_rad
        a = math.sin(dlat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        distance = R * c

        return distance

    filtered_cities = [city for city in city_data if haversine_distance(center_lat, center_lon, city['latitude'], city['longitude']) <= distance]
    total_population = sum(city['population'] for city in filtered_cities)
    total_area = math.pi * (distance ** 2)

    average_density = total_population / total_area

    return average_density