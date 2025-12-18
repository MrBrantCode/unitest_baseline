"""
QUESTION:
Create a function `analyze_license` that takes a string `license_text` as input. The function should identify and categorize the permissions and conditions specified in the license text based on the presence of specific keywords. The keywords are "software", "documentation", "restriction", "rights", "use", "copy", "modify", "merge", "publish", "distribute", "sublicense", "sell", "permit", "persons", "furnished", and "conditions". The function should return two lists: a list of permissions and a list of conditions. Permissions include actions that are allowed, such as "use", "copy", "modify", etc. Conditions are the terms or restrictions associated with the permissions. The function should ignore the keywords "software", "documentation", "rights", "persons", and "furnished" when categorizing permissions and conditions.
"""

def analyze_license(license_text):
    permissions = []
    conditions = []

    keywords = [
        "software", "documentation", "restriction", "rights", "use", "copy", "modify",
        "merge", "publish", "distribute", "sublicense", "sell", "permit", "persons", "furnished", "conditions"
    ]

    for word in license_text.split():
        if word.lower() in keywords:
            if word.lower() in ["software", "documentation", "rights", "persons", "furnished"]:
                continue
            if word.lower() in ["restriction", "conditions"]:
                conditions.append(word.lower())
            else:
                permissions.append(word.lower())

    return permissions, conditions