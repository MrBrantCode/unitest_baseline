"""
QUESTION:
Write a function `extract_license_info` that takes a string as input and returns the extracted license information in the following format:
```
License Type: [extracted license type]
License Text:
[extracted license text]
```
The input string contains the license information in multiple lines, starting with '//' and separated by newline characters. The function should extract the license type from the first line that contains 'Licensed under the' and the license text from all lines starting with '//'. If the license type cannot be extracted, it should default to 'Unknown'.
"""

import re

def extract_license_info(input_string):
    license_type_pattern = r'Licensed under the (.+?)\n'
    license_text_pattern = r'// (.+)'

    license_type_match = re.search(license_type_pattern, input_string)
    license_type = license_type_match.group(1) if license_type_match else "Unknown"

    license_text_matches = re.findall(license_text_pattern, input_string)
    license_text = '\n'.join(license_text_matches)

    return f"License Type: {license_type}\nLicense Text:\n{license_text}"