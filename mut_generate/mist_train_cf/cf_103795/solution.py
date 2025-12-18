"""
QUESTION:
Classify the given data according to their type. The function, `classify_data`, should take in a list of data as input, handle multiple types of data (e.g., integer, float, string), and store the results in a data structure (e.g., dictionary).
"""

def classify_data(data):
    classified_data = {"Integers": [], "Floats": [], "Strings": []}
    
    for item in data:
        if isinstance(item, int):
            classified_data["Integers"].append(item)
        elif isinstance(item, float):
            classified_data["Floats"].append(item)
        elif isinstance(item, str):
            classified_data["Strings"].append(item)
    
    return classified_data