"""
QUESTION:
Organize a list of objects with 'name', 'type', and 'area' properties into a nested dictionary with 'type' and 'area' categories. The 'type' category can have values "fruit", "vegetable", or "dairy", and the 'area' category can have values "North", "South", "East", or "West". The function should return a dictionary where each 'area' contains a list of objects sorted by 'name' in ascending order. If two names are equal, maintain their original sequence. The function should be named `organize_objects` and take a list of objects as input.
"""

def organize_objects(arr):
  """
  Organize a list of objects with 'name', 'type', and 'area' properties into a nested dictionary 
  with 'type' and 'area' categories.

  Args:
    arr (list): A list of objects with 'name', 'type', and 'area' properties.

  Returns:
    dict: A dictionary where each 'area' contains a list of objects sorted by 'name' in ascending order.
  """
  result = {}
  for item in arr:
    if item['type'] not in result:
      result[item['type']] = {}
    if item['area'] not in result[item['type']]:
      result[item['type']][item['area']] = []
    result[item['type']][item['area']].append(item)
  
  for t in result:
    for a in result[t]:
      result[t][a] = sorted(result[t][a], key=lambda x: x['name'])

  return result