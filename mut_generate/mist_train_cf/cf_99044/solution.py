"""
QUESTION:
Create a function `optimize_battery_life` that takes a JSON string as input, where the JSON data represents the power consumption of various components in a handheld gaming console and its battery life. The function should return a JSON string where the usage of each component is optimized to maximize the battery life. The JSON data should be in the following format: 
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
"""

import json
def optimize_battery_life(json_data):
    data = json.loads(json_data)
    total_power_consumption = 0
    for component in data["components"]:
        total_power_consumption += data["components"][component]["power_consumption"] * data["components"][component]["usage"]
    
    for component in data["components"]:
        component_power_consumption = data["components"][component]["power_consumption"] * data["components"][component]["usage"]
        component_usage = (data["battery_life"] / total_power_consumption) * component_power_consumption
        data["components"][component]["usage"] = component_usage
    
    return json.dumps(data)