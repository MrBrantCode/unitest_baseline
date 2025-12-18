"""
QUESTION:
Create a function named `enhanced_match` that accepts two lists of strings. The function should return the list with the lesser total count of characters across all the strings in each list (blank space excluded), while preserving the original sequence of elements in the lists. The function should also eliminate duplicate strings from the lists while only acknowledging the first appearance of every string, and choosing to ignore the case when comparing strings. If both lists have an equal count of characters, the first list should be returned. Additionally, any string in either list containing numbers should be removed prior to the comparison.
"""

def enhanced_match(lst1, lst2):
    # Remove strings that contain numbers
    lst1 = [string for string in lst1 if not any(char.isdigit() for char in string)]
    lst2 = [string for string in lst2 if not any(char.isdigit() for char in string)]
  
    # Remove duplicates, ignoring case
    seen1 = set()
    seen2 = set()
    lst1 = [x for x in lst1 if not (x.lower() in seen1 or seen1.add(x.lower()))]
    lst2 = [x for x in lst2 if not (x.lower() in seen2 or seen2.add(x.lower()))]
  
    # Calculate total character count (excluding blank spaces)
    len1 = sum(len(s.replace(' ', '')) for s in lst1)
    len2 = sum(len(s.replace(' ', '')) for s in lst2)

    # Return the list with the lesser total character count
    if len1 <= len2:
        return lst1
    else:
        return lst2