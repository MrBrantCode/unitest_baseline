"""
QUESTION:
Write a function `compare_versions(predefined_version, user_version)` that compares two version numbers in the format "YYYY.MM.DD" (Year, Month, Day) and returns "Newer" if `user_version` is newer than `predefined_version`, "Older" if `user_version` is older than `predefined_version`, and "Same" if both versions are the same. The function should handle invalid version formats by returning "Invalid version format".
"""

def compare_versions(predefined_version, user_version):
    try:
        predefined_parts = list(map(int, predefined_version.split('.')))
        user_parts = list(map(int, user_version.split('.')))

        if predefined_parts == user_parts:
            return "Same"
        elif predefined_parts < user_parts:
            return "Newer"
        else:
            return "Older"
    except (ValueError, AttributeError):
        return "Invalid version format"