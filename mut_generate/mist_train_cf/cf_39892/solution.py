"""
QUESTION:
Create a function `check_compliance(licenses)` that takes a list of software licenses as input and returns two lists: one containing the compliant licenses and the other containing the non-compliant licenses. A license is considered compliant with the Apache License, Version 2.0 if it contains the phrase "Apache License, Version 2.0" and "you may not use this file except in compliance with the License". The function should use regular expressions to check for the presence of these phrases in each license.
"""

import re

def check_compliance(licenses):
    compliant_licenses = []
    non_compliant_licenses = []
    
    for license in licenses:
        if re.search(r"Apache License, Version 2.0", license) and re.search(r"you may not use this file except in compliance with the License", license):
            compliant_licenses.append(license)
        else:
            non_compliant_licenses.append(license)
    
    return compliant_licenses, non_compliant_licenses