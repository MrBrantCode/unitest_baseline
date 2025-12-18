"""
QUESTION:
Write a function `complex_elements_uniq` that takes a list of elements as input, removes duplicates while maintaining the original order, and handles cases where elements are not exactly the same but considered equal, such as dictionaries with different key orders or nested structures.
"""

import json

def complex_elements_uniq(elements_list):
  # Create an empty list to store the non-duplicate elements
  unique_elements_list = []

  # Create an empty set to store the serialized unique elements
  seen = set()

  for elem in elements_list:
    # We serialize the complex nested structures to handle the edge cases
    serialized_elem = json.dumps(elem, sort_keys=True)

    # Put the element in the output list and the set only if it's not already in the set
    if serialized_elem not in seen:
      seen.add(serialized_elem)
      unique_elements_list.append(elem)
  
  return unique_elements_list