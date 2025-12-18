"""
QUESTION:
Write a function `update_and_extract` that takes a nested dictionary as input and performs the following operations:

- Updates the dictionary with new values for 'age', 'experience_years', and 'university'.
- Extracts the values for 'name', 'role', and 'highest_qualification'.

The input dictionary has the following structure:
{
  'personal_info': {'name': string, 'age': integer},
  'career_info': {'organization': string, 'role': string, 'experience_years': integer},
  'education_info': {'highest_qualification': string, 'university': string}
}

The function should not take any additional arguments other than the dictionary.
"""

def update_and_extract(input_dict):
    # Update the dictionary with new values
    input_dict['personal_info']['age'] = 26
    input_dict['career_info']['experience_years'] = 6
    input_dict['education_info']['university'] = 'ABC University'

    # Extract the values for 'name', 'role', and 'highest_qualification'
    extracted_data = {
        'name': input_dict['personal_info']['name'],
        'role': input_dict['career_info']['role'],
        'highest_qualification': input_dict['education_info']['highest_qualification']
    }
    return extracted_data