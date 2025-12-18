"""
QUESTION:
Write a function `find_holidays_by_locale(dataset, target_locale)` that takes a list of dictionaries `dataset` and a string `target_locale` as input. Each dictionary in the dataset represents a holiday entry with keys 'date', 'description', 'locale', 'notes', 'region', and 'type'. The function should return a list of dictionaries representing holidays observed in the specified locale, sorted by date in ascending order.
"""

def find_holidays_by_locale(dataset, target_locale):
    """
    This function filters holidays by a specific locale and returns them sorted by date.

    Args:
        dataset (list): A list of dictionaries containing holiday entries.
        target_locale (str): The locale to filter holidays by.

    Returns:
        list: A list of dictionaries representing holidays observed in the specified locale, sorted by date in ascending order.
    """

    # Filter holidays by the target locale
    holidays_in_locale = [holiday for holiday in dataset if holiday['locale'] == target_locale]
    
    # Sort holidays by date in ascending order
    sorted_holidays = sorted(holidays_in_locale, key=lambda x: x['date'])
    
    return sorted_holidays