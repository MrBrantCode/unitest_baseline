"""
QUESTION:
Implement a function `modify_version(distribution_name, version_modifier)` that takes a distribution name and a version modifier as input, and returns the modified version of the distribution by inserting the version modifier between the distribution name and the version. If the distribution is not found, return "DistributionNotFound". Assume that the `get_distribution` function retrieves the distribution information based on the distribution name and the distribution version follows the pattern "distribution_name-version".
"""

import re
from pkg_resources import get_distribution, DistributionNotFound

def modify_version(distribution_name, version_modifier):
    try:
        __version_modifier__ = r'(\g<1>)' + version_modifier + r'(\g<2>)'
        version = re.sub(__version_modifier__, r'\g<1>-' + version_modifier + r'-\g<2>', get_distribution(distribution_name).version)
        return version
    except DistributionNotFound:
        return "DistributionNotFound"