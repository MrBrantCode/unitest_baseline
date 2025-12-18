"""
QUESTION:
Write a function `parse_filename` that takes a file name as input and returns a dictionary containing the extracted information from the file name. The file name is in the format "MOD13Q1.AYYYYDDD.hHV.VVV.YYYYMMDDHHMMSS.hdf", where:
- "MOD13Q1" is the product name.
- "YYYY" represents the year in 4 digits.
- "DDD" represents the day of the year in 3 digits.
- "hHV" represents the horizontal tile identifier, where "H" is the horizontal tile number, and "V" is the vertical tile number.
- "VVV" represents the version number.
- "YYYYMMDDHHMMSS" represents the date and time of the file creation.

The function should extract and return the following information from the file name:
1. Product name
2. Year
3. Day of the year
4. Horizontal tile number
5. Vertical tile number
6. Version number
7. Date and time of file creation

The function should return an empty dictionary if the filename does not match the expected pattern.
"""

import re

def parse_filename(filename: str) -> dict:
    pattern = r"MOD13Q1\.A(\d{4})(\d{3})\.h(\d{2})v(\d{2})\.(\d{3})\.(\d{13})\.hdf"
    match = re.match(pattern, filename)
    if match:
        return {
            "product_name": "MOD13Q1",
            "year": int(match.group(1)),
            "day_of_year": int(match.group(2)),
            "horizontal_tile": int(match.group(3)),
            "vertical_tile": int(match.group(4)),
            "version": int(match.group(5)),
            "creation_date_time": match.group(6)
        }
    else:
        return {}