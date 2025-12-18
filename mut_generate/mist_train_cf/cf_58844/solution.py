"""
QUESTION:
Write a function called `checkDataIntegrity` that takes a list of objects as input, where each object contains 'name', 'type', and 'properties' keys. The 'properties' key contains another object with 'color' and 'season' keys. 

The function should first check the integrity of the input data by ensuring each object has the required keys ('name', 'type', 'properties') and only these keys, and that 'properties' has the required keys ('color', 'season') and only these keys. If the data is valid, return True and an empty error message. If the data is invalid, return False and an error message specifying the object with the anomaly.

If the data is valid, sort it based on the 'type', 'color', and 'season' properties in ascending order and return the sorted data. If the data is invalid, return the error message.
"""

def checkDataIntegrity(data):
  for item in data:
    # Checking if all necessary keys are present
    if not all (k in item for k in ("name", "type", "properties")):
      return False, f"{item} is missing some keys."
    # Checking if there are no additional keys
    if any (k not in ("name", "type", "properties") for k in item):
      return False, f"{item} has some additional keys."
    # Checking if all necessary keys are present inside 'properties'
    if not all (k in item["properties"] for k in ("color", "season")):
      return False, f"{item} is missing some keys in 'properties'."
    # Checking if there are no additional keys inside 'properties'
    if any (k not in ("color", "season") for k in item["properties"]):
      return False, f"{item} has some additional keys in 'properties'."
  sortedData = sorted(data, key=lambda x: (x['type'], x['properties']['color'], x['properties']['season']))
  return True, sortedData