"""
QUESTION:
Configure Visual Studio settings from outside the IDE. Implement a function called `configure_vs_settings` to set up Visual Studio IDE settings programmatically. The function should be able to modify settings such as Tools/Options and External Tools. The solution must not require manual intervention within the Visual Studio IDE, as it will be part of a larger script to configure a new PC.
"""

import xml.etree.ElementTree as ET
import os

def configure_vs_settings(vs_version, username, settings):
    """
    Configure Visual Studio IDE settings programmatically.

    Args:
        vs_version (str): The version of Visual Studio.
        username (str): The username of the current user.
        settings (dict): A dictionary of settings to be applied.

    Returns:
        None
    """

    # Define the path to the CurrentSettings.vssettings file
    settings_file_path = f"C:\\Users\\{username}\\Documents\\Visual Studio {vs_version}\\Settings\\CurrentSettings.vssettings"

    # Check if the file exists
    if not os.path.exists(settings_file_path):
        print("The settings file does not exist.")
        return

    # Parse the XML file
    tree = ET.parse(settings_file_path)
    root = tree.getroot()

    # Iterate over the settings and update the values in the XML file
    for category, options in settings.items():
        for option, value in options.items():
            # Find the corresponding element in the XML file
            elem = root.find(f".//Category[@name='{category}']/Category[@name='{option}']")
            if elem is not None:
                # Update the value
                elem.set("value", value)

    # Save the updated XML file
    tree.write(settings_file_path)

# Example usage:
# configure_vs_settings("2019", "username", {
#     "Environment": {
#         "DocumentsLocation": "C:\\Documents",
#     },
#     "Text Editor": {
#         "C#": {
#             "Specific": "value",
#         },
#     },
# })