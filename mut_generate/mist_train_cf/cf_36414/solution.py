"""
QUESTION:
Write a function `analyze_copyright_info(code: str) -> dict` that takes a source code string as input and returns a dictionary containing the extracted copyright information. The copyright information should be in the format:
```
# Copyright <YEAR> <AUTHOR>
# All Rights Reserved.
#
# Author: <AUTHOR> <<EMAIL>>
#
#    Licensed under the <LICENSE>; you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         <LICENSE_URL>
#
```
The dictionary should be in the format:
```
{
    "year": <YEAR>,
    "author": <AUTHOR>,
    "email": <EMAIL>,
    "license": <LICENSE>,
    "license_url": <LICENSE_URL>
}
```
If the copyright information is not found in the input string, return an empty dictionary `{}`.
"""

import re

def analyze_copyright_info(code: str) -> dict:
    pattern = r'Copyright (\d{4}) (.+?)\n# All Rights Reserved\.\n#\n# Author: (.+?) <(.+?)>\n#\n#    Licensed under the (.+?); you may\n#    not use this file except in compliance with the License. You may obtain\n#    a copy of the License at\n#\n#         (.+)\n#'
    match = re.search(pattern, code)
    if match:
        return {
            "year": int(match.group(1)),
            "author": match.group(2),
            "email": match.group(4),
            "license": match.group(5),
            "license_url": match.group(6)
        }
    else:
        return {}