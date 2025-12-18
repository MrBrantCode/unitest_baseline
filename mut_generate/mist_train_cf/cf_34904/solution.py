"""
QUESTION:
Create a function named `parse_config` that takes a string `code_snippet` as input, representing a C++ project configuration file. Extract the following details from the `code_snippet`:

- Description
- URL
- Homepage
- Author (name and email)
- License
- Settings (comma-separated)
- Generators
- Requirements

Restrict the function to use regular expressions for information extraction and return the extracted details in a structured format.
"""

import re

def parse_config(code_snippet):
    """
    Extracts project configuration details from a C++ project configuration file.

    Args:
    code_snippet (str): A string representing the C++ project configuration file.

    Returns:
    dict: A dictionary containing the extracted configuration details.
    """

    # Extracting information using regular expressions
    description = re.search(r'description = "(.*?)"', code_snippet).group(1)
    url = re.search(r'url = "(.*?)"', code_snippet).group(1)
    homepage = re.search(r'homepage = "(.*?)"', code_snippet).group(1)
    author = re.search(r'author = "(.*?)"', code_snippet).group(1)
    license = re.search(r'license = "(.*?)"', code_snippet).group(1)
    settings = re.search(r'settings = (.*?)\n', code_snippet).group(1)
    generators = re.search(r'generators = "(.*?)"', code_snippet).group(1)
    requirements = re.search(r'requires.add\("(.*?)"\)', code_snippet).group(1)

    # Splitting settings into a list
    settings_list = [setting.strip() for setting in settings.replace('"', '').split(',')]

    # Creating a dictionary with the extracted information
    config_details = {
        "description": description,
        "url": url,
        "homepage": homepage,
        "author": author,
        "license": license,
        "settings": settings_list,
        "generators": generators,
        "requirements": requirements
    }

    return config_details