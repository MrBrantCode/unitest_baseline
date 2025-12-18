"""
QUESTION:
Create a function named `process_exoplanet_data` that takes three parameters: `name` (a string representing the exoplanet name), `result` (the result of the data retrieval process), and `iterable` (a boolean indicating whether the result is iterable). The function should return a formatted string containing information about the success of the retrieval, the type of the result, and the length of the result if it is iterable. If an error occurs, the function should return the error message as a string. The function should handle both iterable and non-iterable results, including lists, dictionaries, and integers.
"""

def process_exoplanet_data(name: str, result, iterable: bool) -> str:
    try:
        if iterable:
            result_length = len(result)
        else:
            result_length = None

        return f"exoplanet.{name} success\n\t {type(result)}\n\t {result_length}"
    except Exception as e:
        return str(e)