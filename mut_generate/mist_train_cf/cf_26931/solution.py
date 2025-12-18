"""
QUESTION:
Write a Python function `generate_csv_row` that takes two dictionaries `child_data` and `household_data` as input, representing a child's data and a household's data respectively. The function should return a CSV row as a string with the following fields in the specified order: `case_id`, `owner_id`, `opened_on`, `modified_on`, `name`, `aadhar_number`, `dob`, `died`, `owner_name`, `hh_id`, `hh_name`, `hh_closed_on`. If a property is missing in the input dictionaries, the corresponding field in the CSV row should be populated with an empty string. The `died` field should be converted to a string.
"""

def generate_csv_row(child_data: dict, household_data: dict) -> str:
    csv_row = ','.join([
        child_data.get('case_id', ''),
        child_data.get('owner_id', ''),
        child_data.get('opened_on', ''),
        child_data.get('modified_on', ''),
        child_data.get('name', ''),
        child_data.get('aadhar_number', ''),
        child_data.get('dob', ''),
        str(child_data.get('died', '')),
        household_data.get('owner_name', ''),
        household_data.get('hh_id', ''),
        household_data.get('hh_name', ''),
        household_data.get('hh_closed_on', '')
    ])
    return csv_row