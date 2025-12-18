"""
QUESTION:
Create a function `filter_postal_codes` that retrieves records with a specific postal code pattern from a table. The function should select records where the postal code starts with "32", ends with "12", and has exactly 5 characters. It should also include records where the second character of the postal code is a vowel (A, E, I, O, U).
"""

def filter_postal_codes(records):
    """
    Filter records based on a specific postal code pattern.

    Args:
    records (list): A list of dictionaries containing customer records.

    Returns:
    list: A list of filtered records.
    """
    vowels = 'AEIOU'
    filtered_records = []

    for record in records:
        postal_code = record.get('postal_code')
        
        if (len(postal_code) == 5 and 
            postal_code.startswith('32') and 
            postal_code.endswith('12') and 
            (postal_code[1].upper() in vowels or postal_code[1] in vowels)):
            filtered_records.append(record)

    return filtered_records