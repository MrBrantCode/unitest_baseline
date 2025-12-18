"""
QUESTION:
Create a function named `nums_to_words` that takes a JSON string as input where the keys are integers and values are strings, and returns an HTML unordered list of the corresponding values in ascending order of keys. The function should sort the keys first, then iterate over the sorted keys to construct the HTML list.
"""

import json

def nums_to_words(json_data):
    data = json.loads(json_data)
    nums = sorted([int(key) for key in data.keys()])
    words = "<ul>"
    for num in nums:
        words += "<li>" + data[str(num)] + "</li>"
    words += "</ul>"
    return words