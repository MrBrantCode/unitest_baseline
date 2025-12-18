"""
QUESTION:
Write a function `extract_license_info(code_lines)` that takes a list of strings, each representing a line of code, and returns a dictionary containing the license identifiers as keys and their corresponding license types as values. The license type is determined based on the license identifier: 
- GPL: GNU General Public License
- MIT: MIT License
- Apache: Apache License
- Other: Other License

Ignore leading or trailing whitespaces in the license identifier. The license identifier is in the format "SPDX-License-Identifier: <license_identifier>" and can be found in any line of code.
"""

from typing import List, Dict

def extract_license_info(code_lines: List[str]) -> Dict[str, str]:
    license_info = {}
    for line in code_lines:
        if line.strip().startswith('# SPDX-License-Identifier:'):
            license_identifier = line.strip().split(':')[-1].strip()
            if license_identifier.startswith('GPL'):
                license_info[license_identifier] = 'GNU General Public License'
            elif license_identifier.startswith('MIT'):
                license_info[license_identifier] = 'MIT License'
            elif license_identifier.startswith('Apache'):
                license_info[license_identifier] = 'Apache License'
            else:
                license_info[license_identifier] = 'Other License'
    return license_info