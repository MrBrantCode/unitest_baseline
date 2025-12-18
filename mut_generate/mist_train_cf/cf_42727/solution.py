"""
QUESTION:
Implement the `get_available_pricing_models` function that retrieves the available pricing models for a given combination of underlying asset type and expiry type.

The function takes three parameters: 
- `udl_type` (string): The type of underlying asset, which can be one of the following: 'STOCK', 'FUTURES', 'FX', or 'COMMODITY'.
- `expiry_type` (string): The expiry type, which can be one of the following: 'EUROPEAN' or 'AMERICAN'.
- `object_model` (dictionary): The object model mapping underlying asset types to expiry types and available pricing models.

The function should return a list of available pricing models for the given combination of `udl_type` and `expiry_type`. If no pricing models are found, return an empty list.
"""

def get_available_pricing_models(udl_type, expiry_type, object_model):
    udl_type = udl_type.upper()
    expiry_type = expiry_type.upper()
    
    if udl_type in object_model and expiry_type in object_model[udl_type]:
        return object_model[udl_type][expiry_type]
    else:
        return []