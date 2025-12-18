"""
QUESTION:
Implement a function `is_valid_media_query(query)` that takes a string as input and returns a boolean value indicating whether the string contains a valid complex media query. A valid complex media query starts with "@media " followed by at least one valid media feature and value pair enclosed in parentheses, separated by a colon, and multiple pairs are separated by "and". The media features can be "screen size", "orientation", or "resolution" with specific valid values for each feature.
"""

def is_valid_media_query(query):
    if not query.startswith("@media "):
        return False

    query = query.replace("@media ", "").strip()
    feature_value_pairs = query.split(" and ")
    
    for pair in feature_value_pairs:
        if not pair.startswith("(") or not pair.endswith(")"):
            return False
        
        pair = pair.replace("(", "").replace(")", "").strip()
        if ":" not in pair:
            return False
        
        feature, value = pair.split(":")
        feature = feature.strip()
        value = value.strip()
        
        if feature not in ["screen size", "orientation", "resolution"]:
            return False
        
        if feature == "screen size":
            if value not in ["small", "medium", "large"]:
                return False
        elif feature == "orientation":
            if value not in ["portrait", "landscape"]:
                return False
        elif feature == "resolution":
            if "x" not in value:
                return False
            width, height = value.split("x")
            try:
                width = int(width)
                height = int(height)
                if width <= 0 or height <= 0:
                    return False
            except ValueError:
                return False
    
    return True