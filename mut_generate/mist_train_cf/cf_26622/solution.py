"""
QUESTION:
Create a function `perform_operation` that takes a dictionary `data` as input and returns a new dictionary containing only the "id", "amount", and "timestamp" fields from the input dictionary, if they exist. The function should handle cases where these fields are missing from the input dictionary.

Implement the `perform_operation` function such that it can be used in conjunction with a file processing program that reads a file containing JSON objects, parses each object into a Python dictionary, performs the operation defined in `perform_operation` on each parsed dictionary, and writes the results to an output file, with each result on a new line. The input file is expected to be large, so the implementation should be efficient.
"""

def perform_operation(data):
    # Example operation: Extracting specific fields from the JSON object
    result = {
        "id": data.get("id"),
        "amount": data.get("amount"),
        "timestamp": data.get("timestamp")
    }
    return result