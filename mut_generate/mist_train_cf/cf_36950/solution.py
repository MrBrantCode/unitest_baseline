"""
QUESTION:
Write a function named `extract_license_info` that takes a string `license_text` as input. The function should extract and return a dictionary containing the copyright holder, year(s) covered by the license, and license type from the given license text. The license text is in the format:
```
// Copyright [year]-present [copyright holder].
//
// Licensed under the [license type].
```
Where:
- [year] is a 4-digit integer representing the starting year of the license.
- [copyright holder] is the name of the entity holding the copyright.
- [license type] is the type of license under which the content is released.
"""

import re

def extract_license_info(license_text):
    pattern = r'Copyright (\d{4}-present) (.+?)\.\n//\n// Licensed under the (.+?)\.$'
    match = re.search(pattern, license_text)
    
    if match:
        year = match.group(1)
        holder = match.group(2)
        license_type = match.group(3)
        return {
            "Copyright holder": holder,
            "Year(s) covered by the license": year,
            "License type": license_type
        }
    else:
        return None