"""
QUESTION:
Create a function `optimize_battery_life(json_data)` that takes a JSON string as input, where the JSON data contains information about the power consumption of various components in a handheld gaming console and the battery life. The function should calculate the optimal usage of each component to maximize the battery life based on their power consumption and return the optimized JSON data.

The input JSON data will be in the following format:
```json
{
  "components": {
    "component_name": {
      "power_consumption": float,
      "usage": float
    },
    ...
  },
  "battery_life": float
}
```
The output should be the optimized JSON data with the updated usage of each component.
"""

import json

def optimize_battery_life(json_data):
    # Load the JSON data
    data = json.loads(json_data)
    
    # Calculate the total power consumption
    total_power_consumption = sum(data["components"][component]["power_consumption"] * data["components"][component]["usage"] for component in data["components"])
    
    # Calculate the optimal usage of each component to maximize the battery life
    for component in data["components"]:
        component_usage = (data["battery_life"] / total_power_consumption) * data["components"][component]["power_consumption"] * data["components"][component]["usage"]
        data["components"][component]["usage"] = component_usage
    
    # Return the optimized JSON data
    return json.dumps(data)