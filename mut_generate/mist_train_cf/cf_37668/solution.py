"""
QUESTION:
Create a function named `validate_license` that takes two parameters: `license_agreement` and `license_key`. The function should check if the `license_key` is valid based on the conditions specified in the `license_agreement`. The `license_agreement` should contain the following permissions: "Use", "Copy", "Modify", "Merge", "Publish", "Distribute", "Sublicense", "Sell" and the condition that "The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software." The function should return "Valid" if the `license_key` satisfies all the permissions and conditions, and "Invalid" otherwise.
"""

def validate_license(license_agreement, license_key):
    permissions = ["Use", "Copy", "Modify", "Merge", "Publish", "Distribute", "Sublicense", "Sell"]
    conditions = "The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software."

    # Check if all permissions are present in the license key
    for permission in permissions:
        if permission.lower() not in license_key.lower():
            return "Invalid"

    # Check if the conditions are met
    if conditions.lower() not in license_agreement.lower():
        return "Invalid"

    return "Valid"