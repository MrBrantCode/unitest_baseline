"""
QUESTION:
Create a function `process_shape_data` that takes a file object of JSON data as input and returns a dictionary. The JSON data contains a list of geographical features, each with "RKI_ID" and "RKI_NameDE" properties. The function should extract these properties from each feature, using the "RKI_NameDE" as the key and the "RKI_ID" as the value in the dictionary. The function should be able to handle large datasets efficiently.
"""

import json

def process_shape_data(data_file):
    counties = {}
    shape_data = json.load(data_file)
    for feature in shape_data["features"]:
        id_current = feature["properties"]["RKI_ID"]
        name_current = feature["properties"]["RKI_NameDE"]
        counties[name_current] = id_current
    return counties