"""
QUESTION:
Implement a function `validateApacheLicense` that takes a string `licenseText` as input and returns `True` if the license text complies with the Apache License, Version 2.0, and `False` otherwise. The function must check for the following key elements in the license text: 
1. The license is granted under the Apache License, Version 2.0.
2. The license includes the disclaimer of warranties.
3. The license includes the copyright notice.
4. The license includes the permission notice.
5. The license includes the conditions and limitations specified in the Apache License, Version 2.0.

Function Signature: `def validateApacheLicense(licenseText: str) -> bool`
"""

import re

def validateApacheLicense(licenseText: str) -> bool:
    apache_license_pattern = r"Licensed under the Apache License, Version 2.0"
    disclaimer_pattern = r"You may not use this file except in compliance with the License."
    copyright_pattern = r"Copyright .*"
    permission_pattern = r"You may obtain a copy of the License at .*"
    conditions_pattern = r"Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied."

    return (re.search(apache_license_pattern, licenseText) and 
            re.search(disclaimer_pattern, licenseText) and 
            re.search(copyright_pattern, licenseText) and 
            re.search(permission_pattern, licenseText) and 
            re.search(conditions_pattern, licenseText))