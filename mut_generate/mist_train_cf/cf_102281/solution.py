"""
QUESTION:
Create a function `find_most_common_names` that receives a list of names. Return the name that occurs most frequently in the list. If there is a tie, return all the names in a list, sorted by the number of occurrences in descending order. If the list is empty or contains only one name, return that list or the single name respectively.
"""

def find_most_common_names(names):
    if len(names) <= 1:
        return names
    
    name_counts = {}
    for name in names:
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1
    
    max_count = max(name_counts.values())
    most_common_names = [name for name, count in name_counts.items() if count == max_count]
    
    if len(most_common_names) == 1:
        return most_common_names[0]
    elif len(most_common_names) > 1:
        return sorted(most_common_names, key=lambda name: name_counts[name], reverse=True)
    else:
        return []