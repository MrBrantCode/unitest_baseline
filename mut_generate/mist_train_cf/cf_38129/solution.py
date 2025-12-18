"""
QUESTION:
Implement the `mergeGroupPackages` function, which takes four arguments: a function (`getUniquePackages` or `getCommonPackages`), a collection group (`collgrp`), a script, and a set of seen targets (`seen_targets`). The function should merge the group packages based on the provided function and update the `script.parts` and `script.packages` accordingly.
"""

def mergeGroupPackages(package_function, collgrp, script, seen_targets):
    """
    Merges the group packages based on the provided function and updates the script parts and packages.

    Args:
    package_function (function): The function to use for merging packages (getUniquePackages or getCommonPackages).
    collgrp (collection group): The collection group to merge packages from.
    script (script): The script to update with the merged packages.
    seen_targets (set): The set of seen targets to update with the merged packages.

    Returns:
    tuple: The updated script parts and packages.
    """
    packages = package_function(collgrp)  # Call the provided function with the collection group
    script.parts += packages  # Merge the packages into the script parts
    script.packages.update(packages)  # Update the script packages with the merged packages
    seen_targets.update(packages)  # Update the seen targets with the merged packages
    return script.parts, script.packages  # Return the updated script parts and packages