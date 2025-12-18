"""
QUESTION:
Create a Python class `PackageManager` that handles adding, removing, and listing packages, as well as checking for package dependencies. The class should have the following methods: `__init__`, `add_package`, `remove_package`, `list_packages`, and `check_dependencies`. 

- `__init__` initializes the package manager with an empty list of installed packages.
- `add_package` adds the specified package to the list of installed packages. If the package has dependencies, those dependencies should also be added.
- `remove_package` removes the specified package from the list of installed packages. If the package has dependencies, it should not be removed, and an error message should be displayed.
- `list_packages` returns a list of all installed packages.
- `check_dependencies` returns a list of dependencies for the specified package.

Assume that package dependencies are predefined and provided as a dictionary where the keys are package names and the values are lists of their dependencies.
"""

from typing import List

def package_manager(package_name: str, action: str, dependencies_map: dict, installed_packages: list = None) -> list:
    if installed_packages is None:
        installed_packages = []
    
    if action == 'add':
        if package_name not in installed_packages:
            installed_packages.append(package_name)
        for dependency in dependencies_map.get(package_name, []):
            if dependency not in installed_packages:
                installed_packages.append(dependency)
                
    elif action == 'remove':
        dependencies = dependencies_map.get(package_name, [])
        if dependencies:
            print(f"Error: Cannot remove package {package_name} with dependencies")
        else:
            if package_name in installed_packages:
                installed_packages.remove(package_name)
                
    elif action == 'list':
        return installed_packages
    
    elif action == 'dependencies':
        return dependencies_map.get(package_name, [])

# Assuming dependencies are hardcoded for simplicity
dependencies_map = {
    'weather': [],
    'notice': [],
    'dependency1': [],
    'dependency2': [],
    'dependent_package': ['dependency1', 'dependency2']
}

# Usage
installed_packages = []
installed_packages = package_manager('dependent_package', 'add', dependencies_map, installed_packages)
print(package_manager('dependent_package', 'list', dependencies_map, installed_packages))
print(package_manager('dependent_package', 'dependencies', dependencies_map, installed_packages))