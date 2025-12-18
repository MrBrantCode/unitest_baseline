"""
QUESTION:
Write a function `process_users` that takes a JSON array of user objects as input, where each object contains the user's name, age, and gender. The function should do the following:

- Filter out users whose age is 18 or above and gender is either 'male' or 'female'.
- Calculate the average age of the filtered users.
- Sort the filtered users based on their age in ascending order.
- If any user does not meet the age and gender conditions, print an error message.

The input JSON array is expected to be in the format:
```
[
  {
    "name": string,
    "age": integer,
    "gender": string
  },
  ...
]
```
"""

import json

def process_users(users):
    """
    Process a JSON array of user objects.

    This function filters out users whose age is 18 or above and gender is either 'male' or 'female',
    calculates the average age of the filtered users, sorts the filtered users based on their age in ascending order,
    and prints an error message for any user who does not meet the age and gender conditions.

    Args:
        users (list): A JSON array of user objects.

    Returns:
        tuple: A tuple containing the average age of the filtered users and the sorted list of users.
    """

    # Initialize variables for age and count
    total_age = 0
    count = 0

    # Check age and gender for each user
    for user in users:
        if user['age'] > 18 and user['gender'] in ['male', 'female']:
            total_age += user['age']
            count += 1
        else:
            print(f"Error: Invalid user - Name: {user['name']}, Age: {user['age']}, Gender: {user['gender']}")

    # Calculate and return the average age
    if count > 0:
        average_age = total_age / count
    else:
        average_age = 0

    # Sort users based on age in ascending order
    sorted_users = sorted(users, key=lambda x: x['age'])

    return average_age, sorted_users