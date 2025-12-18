"""
QUESTION:
Write a function `parse_package_metadata(code_snippet: str) -> dict` that takes a string `code_snippet` representing Python package metadata as input and returns a dictionary containing the extracted metadata. The input `code_snippet` is a string representing the Python package metadata with details such as version, packages, URL, license, author, install_requires, classifiers, and author email, spread across multiple lines.

The dictionary returned by the function should have the following keys:
- "version": The version of the package (string).
- "packages": A list of packages included in the package (list of strings).
- "url": The URL of the package (string).
- "license": The license of the package (string).
- "author": The author of the package (string).
- "install_requires": A list of required packages for installation (list of strings).
- "classifiers": A list of classifiers for the package (list of strings).
- "author_email": The email of the author (string).

The function should handle cases where certain metadata fields are empty or not provided in the code snippet.
"""

import ast

def parse_package_metadata(code_snippet: str) -> dict:
    metadata = {}
    try:
        code_snippet = "{" + code_snippet + "}"  # Convert to valid dictionary syntax
        metadata_dict = ast.literal_eval(code_snippet)  # Safely evaluate the dictionary expression
        metadata["version"] = metadata_dict.get("version", "")
        metadata["packages"] = metadata_dict.get("packages", [])
        metadata["url"] = metadata_dict.get("url", "")
        metadata["license"] = metadata_dict.get("license", "")
        metadata["author"] = metadata_dict.get("author", "")
        metadata["install_requires"] = metadata_dict.get("install_requires", [])
        metadata["classifiers"] = metadata_dict.get("classifiers", [])
        metadata["author_email"] = metadata_dict.get("author_email", "")
    except (ValueError, SyntaxError):
        print("Invalid code snippet format")
    return metadata