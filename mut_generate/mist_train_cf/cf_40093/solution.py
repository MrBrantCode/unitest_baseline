"""
QUESTION:
Write a function `parse_schema_output(schema_output: str) -> dict` that takes a string `schema_output` containing a formatted representation of date and time information as input, and returns a dictionary containing the individual components of the date and time, including the day of the week, month, day, time, timezone, and year. The input string is in the format "{dayofweek:xxx, month:xxx, day:xxx, time:xx:xx:xx, timezone:xxx, year:xxxx}". The returned dictionary should have the same keys as the input string, with the values corresponding to the extracted components. The day and year values should be integers, while the other values are strings.
"""

import re

def parse_schema_output(schema_output: str) -> dict:
    pattern = r"(\w+):(\w+), (\w+):(\w+), (\w+):(\d+), (\w+):(\d+:\d+:\d+), (\w+):(\w+), (\w+):(\d+)"
    matches = re.match(pattern, schema_output)
    components = {
        matches.group(1): matches.group(2),
        matches.group(3): matches.group(4),
        matches.group(5): int(matches.group(6)),
        matches.group(7): matches.group(8),
        matches.group(9): matches.group(10),
        matches.group(11): int(matches.group(12))
    }
    return components