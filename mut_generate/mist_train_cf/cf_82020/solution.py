"""
QUESTION:
Create a function `sort_people(people, sort_by)` that takes a list of people and a sorting criterion as input. The list of people contains dictionaries with 'name', 'age', 'city', and 'profession' as keys. The function should return the sorted list of people based on the given sorting criterion, which can be either 'name' or 'age'. The input and output format should be in the string format 'name, age, city, profession'. The function should be case-sensitive to the sorting criterion.
"""

def sort_people(people, sort_by):
    """
    Sorts a list of people based on the given sorting criterion.

    Args:
    people (list): A list of dictionaries containing 'name', 'age', 'city', and 'profession' as keys.
    sort_by (str): The sorting criterion, either 'name' or 'age'.

    Returns:
    list: The sorted list of people in the string format 'name, age, city, profession'.
    """
    return sorted(people, key=lambda x: x[sort_by])

# Example usage:
# people = [
#     {'name': 'John', 'age': 25, 'city': 'New York', 'profession': 'Engineer'},
#     {'name': 'Alice', 'age': 30, 'city': 'London', 'profession': 'Doctor'},
#     {'name': 'Bob', 'age': 20, 'city': 'Paris', 'profession': 'Lawyer'}
# ]
# sorted_people = sort_people(people, 'age')
# for person in sorted_people:
#     print("{}, {}, {}, {}".format(person['name'], person['age'], person['city'], person['profession']))