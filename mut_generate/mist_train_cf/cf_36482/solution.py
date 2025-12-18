"""
QUESTION:
Implement a function named `version_check` that takes three inputs: `self.name`, `installed_version`, and a `version_range` tuple `(min_version, max_version)`, and returns a compatibility message. The message should be "Library version for '{self.name}' is compatible." if the installed version is within the required range, and "Library version for '{self.name}' is incompatible. Installed: {installed_version}, Needed: {min_version} <= x < {max_version}" if it is outside the range.
"""

def version_check(self, installed_version, version_range):
    min_version, max_version = version_range
    if min_version <= installed_version < max_version:
        return "Library version for '{}' is compatible.".format(self.name)
    else:
        return "Library version for '{}' is incompatible. Installed: {}, Needed: {} <= x < {}".format(self.name, installed_version, min_version, max_version)