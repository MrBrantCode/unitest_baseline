"""
QUESTION:
Implement a function named `filter_and_sort` that takes a list of dictionaries as input. The function should filter out dictionaries where the value of the key 'score' is less than 3 or the value of the key 'age' is greater than 50, and then sort the remaining dictionaries in descending order based on the value of the key 'score'. The function should return the sorted list of dictionaries.
"""

def filter_and_sort(lst):
    # filter elements based on 'score' and 'age' criteria
    filtered = [item for item in lst if item['score'] >= 3 and item['age'] <= 50]

    # sort filtered list in descending order by 'score' 
    sorted_lst = sorted(filtered, key=lambda x: x['score'], reverse=True)

    return sorted_lst