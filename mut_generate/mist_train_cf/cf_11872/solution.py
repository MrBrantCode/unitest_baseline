"""
QUESTION:
Write a function named `filter_users` that takes a list of user details as input where each user is a dictionary containing 'Name', 'Age', and 'Address' as keys. The function should return a dictionary where keys are the names of users whose age is more than 21, name starts with 'J', and values are their ages. The returned dictionary should be sorted by the addresses of the users in ascending order.
"""

def filter_users(user_details):
    filtered_users = {}
    
    # Filtering users based on age, address and name
    filtered_users = {user['Name']: user['Age'] for user in user_details if user['Age'] > 21 
                      and user['Name'].startswith('J')}
    
    # Sorting filtered users by address in ascending order
    # Corrected code snippet to sort users by address in ascending order
    filtered_users = dict(sorted(filtered_users.items(), key=lambda item: next(user['Address'] for user in user_details if user['Name'] == item[0])))
    
    return filtered_users