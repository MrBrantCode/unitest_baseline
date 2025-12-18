"""
QUESTION:
Create a Python function `check_package_version(user_version)` that takes a string `user_version` representing a version number in the semantic versioning format (MAJOR.MINOR.PATCH) and compares it to a given latest version. 

The function should return a message indicating whether the user's version is the latest, outdated, or ahead of the latest release.
"""

def check_package_version(user_version):
    latest_version = '0.3.7'  # Replace with the actual latest version
    if user_version == latest_version:
        return "You are using the latest version of the package."
    elif user_version < latest_version:
        return f"Your version is outdated. The latest version is {latest_version}."
    else:
        return f"You seem to be using a version ahead of the latest release. The latest version is {latest_version}."