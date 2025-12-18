"""
QUESTION:
Implement a function `validate_requirements` that takes a list of software requirements and a version number as input and returns a list of requirements that are satisfied by the given version number. The requirements are specified up to the minor version to allow bugfixes to be automatically applied.

The requirements list contains strings in the format "package_name==major.minor" and the version parameter is a string in the format "major.minor.patch". A requirement is considered satisfied if the package name matches and the major and minor version numbers are less than or equal to the corresponding version numbers in the requirement.
"""

def validate_requirements(requirements: list, version: str) -> list:
    satisfied_requirements = []
    major, minor, _ = map(int, version.split('.'))
    
    for req in requirements:
        package, req_version = req.split('==')
        req_major, req_minor = map(int, req_version.split('.'))
        
        if package and major >= req_major and minor >= req_minor:
            satisfied_requirements.append(req)
    
    return satisfied_requirements