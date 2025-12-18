"""
QUESTION:
Write a Python function `extract_sensor_data` that takes a SensorML document as a string, extracts the latitude and longitude from the `Position` element, and returns them as a tuple in the format `(latitude, longitude)`. The SensorML document is an XML string with a `Position` element containing child elements `Latitude` and `Longitude` representing the sensor's geographic coordinates in decimal degrees. The input SensorML document is well-formed and contains the necessary elements. The function should return the extracted latitude and longitude values as a tuple.
"""

import xml.etree.ElementTree as ET

def extract_sensor_data(sensorml_document: str) -> tuple:
    root = ET.fromstring(sensorml_document)
    position = root.find('.//{http://www.opengis.net/sensorML/1.0.1}Position')
    latitude = float(position.find('.//{http://www.opengis.net/sensorML/1.0.1}Latitude').text)
    longitude = float(position.find('.//{http://www.opengis.net/sensorML/1.0.1}Longitude').text)
    return (latitude, longitude)