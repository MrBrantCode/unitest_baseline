"""
QUESTION:
Create a function `validateLicense` that takes a string `licenseText` as input and returns a boolean value indicating whether the license meets the redistribution conditions. The license is valid if it retains the required copyright notice, conditions, and disclaimer for both source code and binary form redistribution, and verifies that the software contributors' names are not used for product endorsement without prior written permission. The function should return `True` if all conditions are met, and `False` otherwise.
"""

import re

def validateLicense(licenseText: str) -> bool:
    # Check if copyright notice, conditions, and disclaimer are retained for source code redistribution
    source_code_conditions_met = re.search(r'Redistributions of source code must retain the above copyright notice', licenseText) is not None
    source_code_conditions_met = source_code_conditions_met and re.search(r'this list of conditions and the following disclaimer', licenseText) is not None

    # Check if copyright notice, conditions, and disclaimer are retained for binary form redistribution
    binary_form_conditions_met = re.search(r'Redistributions in binary form must reproduce the above copyright notice', licenseText) is not None
    binary_form_conditions_met = binary_form_conditions_met and re.search(r'this list of conditions and the following disclaimer in the documentation', licenseText) is not None

    # Check if contributors' names are not used for product endorsement without prior written permission
    endorsement_permission_met = re.search(r'Neither the name of .* nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission', licenseText) is not None

    return source_code_conditions_met and binary_form_conditions_met and endorsement_permission_met