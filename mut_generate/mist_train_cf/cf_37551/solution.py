"""
QUESTION:
Write a function called `filter_locations` that takes two inputs: a dictionary `json_data` containing geographical data and a float `threshold`. The dictionary should have a key "locations" that maps to a list of dictionaries, each representing a location with "longitude", "latitude", "county", and "stateCode" fields. The function should return a list of dictionaries, each containing the "county" and "stateCode" for locations where the absolute difference between the longitude and latitude is greater than the given threshold.
"""

def filter_locations(json_data: dict, threshold: float) -> list:
    filtered_locations = []
    for location in json_data["locations"]:
        abs_diff = abs(location["longitude"] - location["latitude"])
        if abs_diff > threshold:
            filtered_locations.append({"county": location["county"], "stateCode": location["stateCode"]})
    return filtered_locations