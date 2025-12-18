"""
QUESTION:
Write a function `update_vivarium` that takes a vivarium ID, temperature, and humidity as input, and updates the corresponding data in a dictionary. The function should return a success message after the update. The dictionary stores data for multiple vivariums, each identified by a unique ID, and has the keys 'name', 'temperature', and 'humidity'. The function will be used in a Flask web application hosted on a local server. The vivarium data will be displayed on a web page for each vivarium.
"""

def update_vivarium(vivarium_data, vivarium_id, temperature, humidity):
    vivarium_data[vivarium_id]['temperature'] = temperature
    vivarium_data[vivarium_id]['humidity'] = humidity
    return 'Vivarium data updated successfully'