"""
QUESTION:
Create a Python function `process_vessel_data(data)` that takes a list of dictionaries `data` as input. Each dictionary in the list has two keys: "key" and "value", where "key" represents the label of the information and "value" represents the corresponding data. The function should extract the vessel name, coordinates, and position received time, and return a dictionary with the keys "vessel_name", "coordinates", and "position_received_time". The position received time should be in the format "YYYY-MM-DD HH:MM:SS".
"""

from datetime import datetime

def process_vessel_data(data):
    result = {}
    for item in data:
        if item["key"] == "Coordinates":
            result["coordinates"] = item["value"]
        elif item["key"] == "Vessel Name":
            result["vessel_name"] = item["value"]
        elif item["key"] == "Position received":
            time = datetime.strptime(item["value"], '%b %d, %Y %H:%M %Z')
            result["position_received_time"] = time.strftime('%Y-%m-%d %H:%M:%S')
    return result