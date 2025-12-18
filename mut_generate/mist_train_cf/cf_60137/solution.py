"""
QUESTION:
Filter `users` collection by 'age' and 'location' fields, returning objects with age greater than 21 and location 'USA'. The objects should also have an 'email' field with a '.com' or '.org' domain. Sort the results in descending order by 'age' and limit to 10.
"""

def filter_users(users):
    return [user for user in users if 
            user.get('age', 0) > 21 and 
            user.get('location') == 'USA' and 
            (user.get('email', '').endswith('.com') or user.get('email', '').endswith('.org'))]

def sort_and_limit(users):
    return sorted(filter_users(users), key=lambda x: x.get('age', 0), reverse=True)[:10]

# this can be simplified to one function
def entance(users):
    return sorted([user for user in users if 
            user.get('age', 0) > 21 and 
            user.get('location') == 'USA' and 
            (user.get('email', '').endswith('.com') or user.get('email', '').endswith('.org'))], 
            key=lambda x: x.get('age', 0), reverse=True)[:10]