"""
QUESTION:
Design a function called `parse_log_messages` that takes a string of log messages as input and returns a list of tuples. The function should be able to parse log messages in the format "The temperature at P# is ##F." and extract the location number and temperature value from each message. The function should be able to handle multiple messages in the input string and return a list of tuples, where each tuple contains the location number and temperature value.
"""

import re

def parse_log_messages(log_string):
    """
    This function takes a string of log messages as input, parses the messages, 
    and returns a list of tuples containing the location number and temperature value.

    Args:
        log_string (str): A string containing log messages.

    Returns:
        list: A list of tuples, where each tuple contains the location number and temperature value.
    """

    # Define the regex pattern to match the log messages
    pattern = r"The temperature at P(\d+) is (\d+)F."

    # Use the findall function to find all matches of the pattern in the log string
    matches = re.findall(pattern, log_string)

    # Convert the matches to a list of tuples with location number and temperature value
    result = [(int(match[0]), int(match[1])) for match in matches]

    return result