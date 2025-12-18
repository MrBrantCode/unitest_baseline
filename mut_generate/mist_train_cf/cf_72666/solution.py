"""
QUESTION:
Write a function `serialize_deserialize_payload` to handle the serialization and deserialization of payloads in Apache Kafka. The function should take a dictionary as input, convert it into a JSON string, and then deserialize it back into a dictionary. The function should return the deserialized dictionary.

Note: The function should not have any external dependencies other than the built-in Python library.
"""

def serialize_deserialize_payload(payload_dict):
    """
    This function takes a dictionary, converts it into a JSON string, 
    and then deserializes it back into a dictionary.

    Args:
        payload_dict (dict): The dictionary to be serialized and deserialized.

    Returns:
        dict: The deserialized dictionary.
    """
    import json

    # Convert the dictionary into a JSON string
    json_string = json.dumps(payload_dict)

    # Deserialize the JSON string back into a dictionary
    deserialized_dict = json.loads(json_string)

    return deserialized_dict