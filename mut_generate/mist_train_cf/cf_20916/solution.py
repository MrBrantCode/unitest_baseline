"""
QUESTION:
Create a function called `convert_csv_to_json` that takes a string representing a CSV file as input and returns a JSON object. The CSV file has the following structure: the first line contains the headers "city", "country", "latitude", and "longitude", and each subsequent line represents a city with its corresponding data. The function should return a JSON object where each city is represented as a key-value pair, with the city name as the key and an object containing the country, latitude, and longitude as the value. The latitude and longitude values should be parsed as floating-point numbers. The function should handle cases where there are missing fields or extra fields in the CSV data, and it should assume that the city names will be unique.
"""

import csv
import json

def convert_csv_to_json(csv_string):
    lines = csv_string.strip().split('\n')
    headers = lines[0].split(',')
    cities = {}
    
    for line in lines[1:]:
        data = line.split(',')
        city_info = {}
        
        for i, header in enumerate(headers):
            if i < len(data):
                city_info[header] = data[i]
        
        if 'city' in city_info and 'country' in city_info and 'latitude' in city_info and 'longitude' in city_info:
            cities[city_info['city']] = {
                'country': city_info['country'],
                'latitude': float(city_info['latitude']),
                'longitude': float(city_info['longitude'])
            }
    
    return json.dumps(cities, indent=2)