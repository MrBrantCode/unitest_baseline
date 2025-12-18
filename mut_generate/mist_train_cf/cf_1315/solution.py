"""
QUESTION:
Write a function `combine_lists` that takes two lists of dictionaries and returns a new list of dictionaries. The function should combine the two lists, filter out any dictionaries where the age is less than 21 and add a key-value pair with key "status" and value "Underage" to these dictionaries, and sort the final list in descending order based on the name attribute (case-insensitive) and then by gender in ascending order. The input lists contain dictionaries with keys 'name', 'age', and 'gender' of type str, int, and str respectively.
"""

from typing import List, Dict, Any

def combine_lists(list1: List[Dict[str, Any]], list2: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    combined_list = list1 + list2
    for i in range(len(combined_list)):
        if combined_list[i]['age'] < 21:
            combined_list[i]['status'] = 'Underage'
    combined_list.sort(key=lambda x: (x['name'].lower(), x['gender']), reverse=True)
    return combined_list