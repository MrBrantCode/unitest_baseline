"""
QUESTION:
Write a function named `convert_to_floats` that takes a list of strings as input and returns a dictionary with the results. The function should attempt to convert each string into a float, handle potential `ValueError` exceptions, and track the number of successful and failed conversions. The returned dictionary should contain the total number of conversions, the number of successful conversions, the number of failed conversions, the list of successful float conversions, and a dictionary mapping failed strings to their corresponding error messages.
"""

def convert_to_floats(list_of_strings):
    successful_conversions = []
    failed_conversions = {}
    success_count = 0
    fail_count = 0
    for item in list_of_strings:
        try:
            successful_conversions.append(float(item))
            success_count += 1
        except ValueError as e:
            failed_conversions[item] = str(e)
            fail_count += 1
    summary = {
        'total': len(list_of_strings),
        'success': success_count,
        'failed': fail_count,
        'conversions': successful_conversions,
        'errors': failed_conversions,
    }
    return summary