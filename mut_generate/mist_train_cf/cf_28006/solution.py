"""
QUESTION:
Implement a functional programming pipeline that consists of three operations: filtering, mapping, and registering. 

Create functions for `custom_filter`, `custom_map`, and `custom_register` with the following requirements: 
- `custom_filter(predicate, data)` filters a collection based on a given predicate and returns the filtered data.
- `custom_map(mapping_function, data)` maps the elements of a collection to a new form using a given mapping function and returns the mapped data.
- `custom_register(data)` registers the processed data or operations for further use.

Demonstrate the usage of these functions in a specific scenario.
"""

# Define the filter function
def custom_filter(predicate, data):
    return list(filter(predicate, data))

# Define the map function
def custom_map(mapping_function, data):
    return list(map(mapping_function, data))

# Define the register function
def custom_register(data):
    # Perform registration logic here
    print("Registered:", data)