"""
QUESTION:
Implement the `check_version` function, which takes two string arguments `installed_version` and `latest_version`, each representing a version number in the format of "x.x.x". If `installed_version` is not equal to `latest_version`, raise a custom exception `NotLatestVersion` with `latest_version` as an argument. If `installed_version` is equal to `latest_version`, return "Latest version installed". The `NotLatestVersion` class should be defined to store the `latest_version` for later reference.
"""

class NotLatestVersion:
    """
    The installed version is not the latest available version
    """
    def __init__(self, latest_version):
        self.latest_version = latest_version

def check_version(installed_version, latest_version):
    if installed_version != latest_version:
        raise NotLatestVersion(latest_version)
    else:
        return "Latest version installed"