"""
QUESTION:
Define a function `collect_unique_values` that takes a list of dictionaries as input, where each dictionary contains "key" and "price" fields. The function should return a list of unique "key" values that have at least 3 characters, sorted in descending order based on the "price" field. If two values have the same price, they should be sorted in ascending order based on their names. The function should handle cases where the list is empty or contains dictionaries with missing or invalid "key" or "price" fields. The "key" field is a string and the "price" field is a number.
"""

def collect_unique_values(lst):
    unique_values = {}
    
    for d in lst:
        if "key" in d and isinstance(d["key"], str) and len(d["key"]) >= 3:
            if "price" in d and isinstance(d["price"], (int, float)):
                key = d["key"]
                price = d["price"]
                
                if key not in unique_values:
                    unique_values[key] = price
                else:
                    if price > unique_values[key]:
                        unique_values[key] = price
                    elif price == unique_values[key]:
                        if key < min(unique_values, key=unique_values.get):
                            unique_values[key] = price
            else:
                continue
        else:
            continue
    
    sorted_values = sorted(unique_values.items(), key=lambda x: (-x[1], x[0]))
    result = [value[0] for value in sorted_values]
    return result