"""
QUESTION:
Create a function `countLicenseConditions` that takes a string `licenseText` as input, extracts and counts the occurrences of unique license conditions denoted by `//` followed by the condition itself, and returns a dictionary where the keys are the unique license conditions and the values are their counts. Each condition should include the entire text following `//` on the same line, and the input string `licenseText` may contain multiple lines.
"""

def countLicenseConditions(licenseText: str) -> dict:
    conditions = {}
    lines = licenseText.split('\n')
    for line in lines:
        if line.startswith('//'):
            condition = line[2:].strip()
            if condition in conditions:
                conditions[condition] += 1
            else:
                conditions[condition] = 1
    return conditions