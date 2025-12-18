"""
QUESTION:
Implement the `advanced_monotonic` function that determines if the elements in a given list are monotonically ascending or descending, considering both strict and non-strict conditions. The function should handle lists containing non-integer or non-float elements by attempting to convert strings to floats and ignoring or returning False if unsuccessful. The function should take a list `l` and an optional boolean parameter `strict` (defaulting to False), and return a boolean indicating whether the list is monotonically ascending or descending.
"""

def advanced_monotonic(l: list, strict: bool = False):
    cleaned = []
    # Remove non-integer or non-float elements
    for item in l:
        if isinstance(item, (int, float)):
            cleaned.append(item)
        else:
            try: # Assume it might be a string that can convert to a float
                cleaned.append(float(item))
            except ValueError: # If converting string to float fails, return False
                return False

    if len(cleaned) <= 1: # If list became empty or only has a single element left, it's technically monotonic
        return True

    if strict:
        return all(x < y for x, y in zip(cleaned, cleaned[1:])) \
               or all(x > y for x, y in zip(cleaned, cleaned[1:]))
    else:
        return all(x <= y for x, y in zip(cleaned, cleaned[1:])) \
               or all(x >= y for x, y in zip(cleaned, cleaned[1:]))