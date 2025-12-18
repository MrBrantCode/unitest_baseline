"""
QUESTION:
Create a function `process_dependencies(install_requires)` that takes a list of package dependencies in a specific format as input. Each item in the list is either a single package name or a string in the format `"package_name: dependency1, dependency2, ..."`. The function should return a dictionary where each key is a package name and its corresponding value is a list of its dependencies. 

The input list `install_requires` contains items with the following restrictions: 
- A package with no dependencies is listed as a single string.
- A package with dependencies is listed as a string in the format `"package_name: dependency1, dependency2, ..."`. 

For example, given the input list `["fitbit", "requests", "oauthlib", "fitbit: requests, oauthlib", "requests: urllib3", "urllib3: certifi"]`, the function should return `{"fitbit": ["requests", "oauthlib"], "requests": ["urllib3"], "urllib3": ["certifi"]}`.
"""

def process_dependencies(install_requires):
    dependencies_dict = {}
    for item in install_requires:
        if ':' in item:
            package, dependencies = item.split(':')
            dependencies_dict[package.strip()] = [dep.strip() for dep in dependencies.split(',')]
        else:
            dependencies_dict[item] = []
    return dependencies_dict