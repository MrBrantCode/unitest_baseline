"""
QUESTION:
Create a function `get_developers` that takes a list of dictionaries, where each dictionary represents a person with fields "name", "age", and "job". The function should return a new list containing only the persons with the 'job' field as 'developer'. The returned list should only consist of the 'name' and 'age' fields. The function should handle erroneous data by checking for the presence of necessary keys in each dictionary.
"""

def get_developers(person_list):
    dev_list = [{'name': p['name'], 'age': p['age']} 
                for p in person_list 
                if 'name' in p and 'age' in p and 'job' in p and p['job'] == 'developer']
    return dev_list