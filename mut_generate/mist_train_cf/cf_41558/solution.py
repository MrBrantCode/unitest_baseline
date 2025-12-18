"""
QUESTION:
Implement a `VersionManager` class with the following requirements: 

- The class should have a constructor that takes a version string as input and stores it internally. 
- The class should have methods `is_equal`, `is_greater`, and `is_lesser` that compare the stored version with another version string and return a boolean value indicating whether the two versions are equal, greater, or lesser, respectively.
- The class should have a method `latest_version` that takes a list of version strings as input and returns the latest version from the list.

The version strings follow the semantic versioning format (e.g., "1.2.3").
"""

def is_greater(version1, version2):
    return version1 > version2

def is_lesser(version1, version2):
    return version1 < version2

def is_equal(version1, version2):
    return version1 == version2

def latest_version(versions):
    return max(versions)