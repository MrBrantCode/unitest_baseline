"""
QUESTION:
Implement the function `count_package_versions(packages)` that takes a list of strings representing Python packages with their version numbers and returns a dictionary containing the count of each package's major version. The major version is the first digit in the version number. Packages without version numbers should be counted as None.
"""

def count_package_versions(packages):
    version_counts = {}
    for package in packages:
        parts = package.split(">=")
        if len(parts) == 2:
            version = parts[1].split(".")[0]
            if version.isdigit():
                version = int(version)
                version_counts[version] = version_counts.get(version, 0) + 1
            else:
                version_counts[None] = version_counts.get(None, 0) + 1
        else:
            version_counts[None] = version_counts.get(None, 0) + 1
    return version_counts