"""
QUESTION:
Write a function `satisfies_dependency(package_version, dependency_declaration, condition)` that takes in the package version, a dependency declaration, and an optional condition, and returns `True` if the package version satisfies the dependency declaration with the given condition, and `False` otherwise. 

The dependency declaration syntax is `'<package>@<min_version>:<max_version>'` and the condition syntax is `'<condition_version>-<package_version>-<platform>-<architecture>'`. The package version syntax is `<package>@<version>`. The function should first check if the package name in the package version matches the package name in the dependency declaration. Then it should check if the version in the package version satisfies the version range in the dependency declaration. If a condition is provided, it should check if the package version, platform, and architecture match the condition. 

The function should return `True` if all checks pass, and `False` otherwise.
"""

import re

def satisfies_dependency(package_version: str, dependency_declaration: str, condition: str = None) -> bool:
    package, version_range = dependency_declaration.split('@')
    min_version, max_version = version_range.split(':')
    
    # Check if the package matches
    if package != package_version.split('@')[0]:
        return False
    
    # Check if the version satisfies the range
    version = package_version.split('@')[1]
    if not (min_version <= version <= max_version):
        return False
    
    # Check the condition if provided
    if condition:
        condition_pattern = re.compile(r'@(\d+\.\d+\.\d+\.\d+)-(\d+\.\d+)-(\w+)-(\w+)')
        match = condition_pattern.match(condition)
        if match:
            condition_version = match.group(1)
            condition_platform = match.group(3)
            condition_architecture = match.group(4)
            
            package_version = package_version.split('@')[1]
            package_platform = condition.split('-')[-2]
            package_architecture = condition.split('-')[-1]
            
            if not (package_version == condition_version and package_platform == condition_platform and package_architecture == condition_architecture):
                return False
        else:
            return False
    
    return True