"""
QUESTION:
Create a function named `fix_application_names` that takes a list of application names as input and returns a new list with the names corrected. The function should correct common spelling and capitalization errors in the names, matching the most widely accepted spellings. The corrected list should maintain the same order as the input list.
"""

def fix_application_names(apps: list) -> list:
    corrected_apps = []
    for app in apps:
        if app == "google-chorme":
            corrected_apps.append("google-chrome")
        elif app == "spotfiy":
            corrected_apps.append("spotify")
        else:
            corrected_apps.append(app)
    return corrected_apps