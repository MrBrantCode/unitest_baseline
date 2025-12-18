"""
QUESTION:
Create a function `extract_function_names` that takes a JSON string representing a smart contract's ABI as input, where the ABI is an array of objects with each object containing "type" and "name" fields. The function should extract and return the names of all the objects with "type" as "function". The input JSON string is a multi-line string and the ABI objects are not wrapped in a list, so the input string needs to be wrapped in a list before parsing.
"""

import json

def extract_function_names(abi_json):
    """
    Extracts and returns the names of all the functions from a given ABI JSON string.

    Args:
        abi_json (str): A JSON string representing a smart contract's ABI.

    Returns:
        list: A list of function names.
    """
    # Wrap the input string in a list before parsing
    abi_data = json.loads("[" + abi_json + "]")
    # Extract the names of all the functions
    return [item["name"] for item in abi_data if item["type"] == "function"]