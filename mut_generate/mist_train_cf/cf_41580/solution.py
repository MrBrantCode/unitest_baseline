"""
QUESTION:
Write a Python function `parse_dependencies` that takes a string representing the content of a `setup.py` file as input and returns a dictionary containing the dependencies and their links. The function should parse the `install_requires` and `dependency_links` sections from the input string and handle cases where these sections are not present. The output dictionary should be in the format `{'dependencies': [...], 'dependency_links': [...]}`.
"""

import re

def parse_dependencies(setup_content):
    dependencies = []
    dependency_links = []

    install_requires_match = re.search(r'install_requires=\[(.*?)\]', setup_content, re.DOTALL)
    if install_requires_match:
        dependencies = re.findall(r"'(.*?)'", install_requires_match.group(1))

    dependency_links_match = re.search(r'dependency_links=\[(.*?)\]', setup_content, re.DOTALL)
    if dependency_links_match:
        dependency_links = re.findall(r'"(.*?)"', dependency_links_match.group(1))

    return {
        'dependencies': dependencies,
        'dependency_links': dependency_links
    }