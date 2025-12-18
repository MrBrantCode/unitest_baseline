"""
QUESTION:
Create a function called `merge_dicts` that takes two dictionaries `dict1` and `dict2` as input and returns a new dictionary. The function should merge `dict1` and `dict2` into one dictionary, incrementing the values of common keys. The resulting dictionary should be sorted by its keys. The function should handle any exceptions that occur during execution. The keys of the input dictionaries can be either strings or integers.
"""

def merge_dicts(dict1, dict2):
    try:
        result = dict1.copy()
        for key, value in dict2.items():
            if key in result:
                result[key] += value
            else:
                result[key] = value
        result = dict(sorted(result.items()))
        return result
    except Exception as e:
        print(f"An error occurred: {e}")