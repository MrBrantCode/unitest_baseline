"""
QUESTION:
Create a function `sort_and_filter(data)` that takes a list of dictionaries `data` where each dictionary contains `name` and `public_id` as keys. The function should return a list of dictionaries where the name starts with a vowel (case-insensitive) and sorted in descending order by `public_id`.
"""

def sort_and_filter(data):
    vowels = ['A', 'E', 'I', 'O', 'U']
    return sorted([item for item in data if item['name'][0].upper() in vowels], key=lambda x: x['public_id'], reverse=True)