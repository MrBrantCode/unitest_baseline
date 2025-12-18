"""
QUESTION:
Write a function `manage_package` that takes a dictionary `package_info` as input and returns a formatted string representing the package management information. The dictionary may contain the following keys: `DEPENDS`, `BREAKS`, `REPLACES`, and `EXTRA_CONFIGURE_ARGS`. The output string should be in a specific format and should only include the sections corresponding to the keys present in the input dictionary.
"""

def manage_package(package_info):
    package_name = "Termux"
    dependencies = package_info.get("DEPENDS", "")
    conflicts = package_info.get("BREAKS", "")
    replaces = package_info.get("REPLACES", "")
    extra_configure_args = package_info.get("EXTRA_CONFIGURE_ARGS", "")

    output = f"Package: {package_name}\n"
    if dependencies:
        output += f"Dependencies: {dependencies}\n"
    if conflicts:
        output += f"Conflicts: {conflicts}\n"
    if replaces:
        output += f"Replaces: {replaces}\n"
    if extra_configure_args:
        output += f"Extra Configure Args: {extra_configure_args}\n"

    return output.strip()