"""
QUESTION:
Create a function `parse_license_info` that takes a string `info` as input, where the string is in the format "maintainer <<EMAIL>>:license_type:parameters", and returns a dictionary containing the parsed information with keys "maintainer", "email", "license_type", and "parameters". The function should assume that the input string will always follow the specified format and the maintainer's name and email, as well as the license type and its parameters, will not contain any special characters other than alphanumeric characters and spaces.
"""

def parse_license_info(info):
    maintainer, license_info = info.split(" <<EMAIL>>:")
    license_type, parameters = license_info.split(":")
    return {
        "maintainer": maintainer,
        "email": "<<EMAIL>>",
        "license_type": license_type,
        "parameters": parameters
    }