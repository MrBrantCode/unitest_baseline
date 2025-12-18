"""
QUESTION:
Implement the `__output_json` function that takes two dictionaries as input: `vehicle_id_to_destination` and `vehicle_id_to_planned_route`. The function should return a JSON string where the keys are vehicle IDs (strings) and the values are tuples of latitude and longitude coordinates for destinations and lists of tuples for planned routes.

The JSON output should have the structure:
```json
{
  "vehicles": [
    {
      "id": "vehicle_id",
      "destination": {
        "latitude": latitude,
        "longitude": longitude
      },
      "planned_route": [
        {
          "latitude": latitude,
          "longitude": longitude
        },
        ...
      ]
    },
    ...
  ]
}
```
Assume `vehicle_id_to_destination` and `vehicle_id_to_planned_route` are already defined and have the required keys and values.
"""

import json

def entrance(vehicle_id_to_destination, vehicle_id_to_planned_route):
    vehicles = []
    for vehicle_id, destination in vehicle_id_to_destination.items():
        planned_route = vehicle_id_to_planned_route[vehicle_id]
        route_json = [{"latitude": lat, "longitude": lon} for lat, lon in planned_route]
        vehicle_json = {
            "id": vehicle_id,
            "destination": {
                "latitude": destination[0],
                "longitude": destination[1]
            },
            "planned_route": route_json
        }
        vehicles.append(vehicle_json)
    output_json = {"vehicles": vehicles}
    return json.dumps(output_json, indent=2)