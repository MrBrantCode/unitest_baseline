"""
QUESTION:
Create a function `calculate_median(collection)` that takes a collection of numbers as input and returns the median. The function should handle the following cases: 

- If the collection is empty, return "Error: Empty Collection".
- If the collection contains non-numeric values, return "Error: Non-Numeric Values Exist In The Collection".
- If the collection has an even number of elements, the median is the average of the two middle numbers.
- If the collection has an odd number of elements, the median is the middle number.

The function should not assume any specific type for the collection (e.g., list, tuple, etc.).
"""

def calculate_median(collection):
    try:
        sorted_collection = sorted(collection)
        length = len(sorted_collection)
        
        if length == 0:
            return "Error: Empty Collection"

        if length % 2 == 0:
            median = (sorted_collection[length // 2] + sorted_collection[length // 2 - 1]) / 2
        else:
            median = sorted_collection[length // 2]

        return median

    except TypeError:
        return "Error: Non-Numeric Values Exist In The Collection"