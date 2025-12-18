"""
QUESTION:
Write a function named `extract_api_info` that takes a JSON string `api_response` as input. The function should extract the total number from the "meta" section, the status code from the "headers" section, and the remaining rate limit from the "headers" section. The function should return a dictionary containing the extracted information. 

The input JSON string is guaranteed to have the following structure:
- The "meta" section includes a key-value pair with the key "total" and an integer value.
- The "headers" section includes key-value pairs with the keys "status" and "ratelimit-remaining".

The function should be able to handle different API responses with similar structures and extract the required information accurately.
"""

import json

def extract_api_info(api_response):
    """
    Extracts the total number from the "meta" section, 
    the status code from the "headers" section, and 
    the remaining rate limit from the "headers" section.

    Args:
        api_response (str): A JSON string representing the API response.

    Returns:
        dict: A dictionary containing the extracted information.
    """
    response_data = json.loads(api_response)
    return {
        "total": response_data["meta"]["total"],
        "status_code": response_data["headers"]["status"],
        "remaining_rate_limit": response_data["headers"]["ratelimit-remaining"]
    }