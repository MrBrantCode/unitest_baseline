"""
QUESTION:
Create a function named `find_strings` that takes a list of strings `lst` and a target string `target` as inputs. 

The function should return a list of tuples where each tuple consists of a string from the list and a boolean value indicating whether the string contains the target string. 

The function should return an empty list if the target string is empty or contains only whitespace characters, or if the list of strings is empty or contains only empty or whitespace strings. 

Additionally, the function should handle duplicate strings in the list by returning only one tuple for each unique string.
"""

def find_strings(lst, target):
    if target.strip() == "":
        return []
    
    if not any(lst) or all(s.strip() == "" for s in lst):
        return []
    
    result = []
    seen = set()
    
    for s in lst:
        if s in seen:
            continue
        
        contains_target = target in s
        
        result.append((s, contains_target))
        
        seen.add(s)
    
    return result