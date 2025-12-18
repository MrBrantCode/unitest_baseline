"""
QUESTION:
Write a function `filter_and_sort_records` that filters out records from a given list of objects who are older than 18 years old, have a last name starting with the letter "S", and have a middle name starting with the letter "A". If a record does not have a middle name, it should be considered as not meeting the filtering criteria. The filtered records should then be sorted in ascending order based on age, and if two or more records have the same age, they should be sorted based on their last names in alphabetical order.
"""

def filter_and_sort_records(records):
    """
    Filters out records from a given list of objects who are older than 18 years old, 
    have a last name starting with the letter "S", and have a middle name starting with the letter "A".
    The filtered records are then sorted in ascending order based on age, and if two or more records have the same age, 
    they are sorted based on their last names in alphabetical order.

    Args:
        records (list): A list of dictionaries containing 'name' and 'age' keys.

    Returns:
        list: The filtered and sorted list of records.
    """

    # Filter records based on the given criteria
    filtered_records = [record for record in records 
                        if record['age'] > 18 
                        and len(record['name'].split()) == 3 
                        and record['name'].split()[-1][0].lower() == 's' 
                        and record['name'].split()[1][0].lower() == 'a']

    # Sort the filtered records based on age and last name
    sorted_records = sorted(filtered_records, key=lambda x: (x['age'], x['name'].split()[-1]))

    return sorted_records