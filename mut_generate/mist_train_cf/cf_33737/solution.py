"""
QUESTION:
Create a function `package_info` that takes a string `package_name` as input and returns a dictionary containing the version and license information of the specified package. The package is assumed to be installed in the current Python environment. If the package is not found, the function should return `None`.
"""

import importlib.metadata

def package_info(package_name):
    try:
        package_version = importlib.metadata.version(package_name)
        package_license = importlib.metadata.metadata(package_name)['License']
        return {'version': package_version, 'license': package_license}
    except importlib.metadata.PackageNotFoundError:
        return None