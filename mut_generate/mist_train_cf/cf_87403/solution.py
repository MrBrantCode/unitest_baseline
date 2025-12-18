"""
QUESTION:
Implement a function `is_valid_media_query(query)` that takes in a string `query` as input and returns a boolean value indicating whether the string contains a valid complex media query. A valid complex media query should start with "@media " and contain at least one valid media feature and value pair enclosed in parentheses. Valid media features and values are:
- "screen size" with values "small", "medium", "large"
- "orientation" with values "portrait", "landscape"
- "resolution" with any digit value
- "device type" with values "mobile", "tablet", "desktop"
Multiple media feature and value pairs should be separated by the logical operator "and" or "or".
"""

def is_valid_media_query(query):
    # Check if the query starts with "@media"
    if not query.startswith("@media "):
        return False

    # Remove the "@media " part from the query
    query = query[7:]

    # Split the query by "and" or "or"
    query_parts = query.split(" and ") if " and " in query else query.split(" or ")

    # Iterate over each query part
    for part in query_parts:
        # Split the part into media feature and value
        feature, value = part.strip()[1:-1].split(":")
        feature = feature.strip()
        value = value.strip()

        # Check if the media feature and value are valid
        if feature not in ["screen size", "orientation", "resolution", "device type"]:
            return False
        if feature == "screen size" and value not in ["small", "medium", "large"]:
            return False
        if feature == "orientation" and value not in ["portrait", "landscape"]:
            return False
        if feature == "resolution" and not value.replace("x", "").isdigit():
            return False
        if feature == "device type" and value not in ["mobile", "tablet", "desktop"]:
            return False

    return True