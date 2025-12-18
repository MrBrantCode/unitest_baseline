"""
QUESTION:
Implement the `parse_forecast_response` function to parse a JSON response and extract daily forecast data. The JSON response contains forecast data in the "forecast" field with "simpleforecast" and "forecastday" subfields. Each "forecastday" contains a "date" field with an "epoch" value representing the start time of the forecast. Update the issue date best guess, initially set to the current date and time, to the earliest start time encountered during parsing.

The function should take a JSON response as input and return the issue date best guess as a datetime object. The function should not take any other parameters.
"""

import json
import datetime

def parse_forecast_response(json_response):
    """
    Parse a JSON response and extract daily forecast data.
    
    Args:
    json_response (str): JSON response containing forecast data.
    
    Returns:
    datetime.datetime: The issue date best guess as a datetime object.
    """
    json_result = json.loads(json_response)
    issue_date_best_guess = datetime.datetime.now()

    for daily_forecast in json_result["forecast"]["simpleforecast"]["forecastday"]:
        start_time = datetime.datetime.fromtimestamp(float(daily_forecast["date"]["epoch"]))
        issue_date_best_guess = min(issue_date_best_guess, start_time)

    return issue_date_best_guess