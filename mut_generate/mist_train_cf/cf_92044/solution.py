"""
QUESTION:
Write a function `filter_users` that takes a list of user details as input. Each user detail is a dictionary containing 'Name', 'Age', and 'Address' as keys. The function should filter out users whose age is more than 21 and whose name starts with the letter 'J'. Then, it should sort the filtered users by their addresses in ascending order. Finally, return a dictionary where the keys are the names of the filtered users and the values are their ages. The input list and the output dictionary should not include users whose names do not start with 'J'.
"""

def filter_users(user_details):
    # Filtering users based on age and name
    filtered_users = {user['Name']: user for user in user_details if user['Age'] > 21 and user['Name'].startswith('J')}
    
    # Sorting filtered users by address in ascending order
    filtered_users = dict(sorted(filtered_users.items(), key=lambda x: x[1]['Address']))
    
    # Creating the final output dictionary with names as keys and ages as values
    filtered_users = {key: value['Age'] for key, value in filtered_users.items()}
    
    return filtered_users