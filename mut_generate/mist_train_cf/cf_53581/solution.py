"""
QUESTION:
Write a function named `analyze_dict` that takes in a dictionary as input and returns its metadata. The function should be able to handle nested dictionaries and track the total number of keys, total number of values, total number of unique values, the maximum and minimum value (considering numerical values only), and the level of nesting. The function should also handle potential exceptions that may occur during execution.
"""

def analyze_dict(data, depth=0, metadata=None):
    if metadata is None:
        metadata = {
            "total_keys": 0,
            "total_values": 0,
            "unique_values": set(),
            "nesting_level": 0,
            "min_value": float('inf'),
            "max_value": float('-inf'),
        }
        
    metadata["nesting_level"] = max(metadata["nesting_level"], depth)
      
    for key, value in data.items():
        metadata["total_keys"] += 1
        
        if isinstance(value, dict):
            analyze_dict(value, depth + 1, metadata)
        else:
            metadata["total_values"] += 1
            metadata["unique_values"].add(value)
            
            if isinstance(value, (int, float)):
                metadata["min_value"] = min(metadata["min_value"], value)
                metadata["max_value"] = max(metadata["max_value"], value)
    
    metadata["total_unique_values"] = len(metadata["unique_values"])
    
    return metadata