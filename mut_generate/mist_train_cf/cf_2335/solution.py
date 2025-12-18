"""
QUESTION:
Write a function named `find_second_oldest_age` that takes a list of dictionaries as input, where each dictionary represents a person with an 'age' key. The function should return the age of the second oldest person in the list. If there is a tie for second oldest, return the age of the oldest person among those tied. The age of each person must be a positive integer between 18 and 100 (inclusive). If the input list is empty or does not contain at least two valid 'age' values, return None. The function must have a time complexity of O(n), where n is the length of the input list, and must not use any built-in sorting functions or libraries.
"""

def find_second_oldest_age(people):
    if len(people) < 2:
        return None

    oldest_age = float('-inf')
    second_oldest_age = float('-inf')

    for person in people:
        age = person.get('age')
        if age and isinstance(age, int) and 18 <= age <= 100:
            if age > oldest_age:
                second_oldest_age = oldest_age
                oldest_age = age
            elif age > second_oldest_age and age != oldest_age:
                second_oldest_age = age

    return second_oldest_age if second_oldest_age != float('-inf') else None