"""
QUESTION:
Create a function `update_vivarium` that updates the temperature and humidity data for a specified vivarium in the `vivarium_data` dictionary. The function should accept three parameters: `vivarium_id`, `temperature`, and `humidity`. It should update the dictionary with the new data and return a success message. Assume the dictionary has the following structure: 
```python
vivarium_data = {
    'vivarium_id': {'name': 'Vivarium Name', 'temperature': temperature_value, 'humidity': humidity_value}
}
```
"""

def update_vivarium(vivarium_id, temperature, humidity):
    vivarium_data[vivarium_id]['temperature'] = temperature
    vivarium_data[vivarium_id]['humidity'] = humidity

    return 'Vivarium data updated successfully'