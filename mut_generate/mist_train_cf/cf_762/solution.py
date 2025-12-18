"""
QUESTION:
Implement the `serialize_and_deserialize` function in Python to demonstrate data serialization and deserialization, ensuring performance optimizations, cross-platform compatibility, and support for custom object serialization.
"""

import pickle

def serialize_and_deserialize(obj):
    """
    This function demonstrates data serialization and deserialization using Python's pickle module.
    
    Args:
        obj (object): The object to be serialized and deserialized.
    
    Returns:
        object: The deserialized object.
    """
    
    # Serialize the object into a byte stream
    serialized_obj = pickle.dumps(obj)
    
    # Deserialize the byte stream back into an object
    deserialized_obj = pickle.loads(serialized_obj)
    
    return deserialized_obj