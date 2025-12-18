"""
QUESTION:
Write a function called `filter_users` that takes a list of user details as input, where each user is a dictionary containing 'name', 'age', 'occupation', and 'address'. Filter the users to include only those whose age is more than 25, occupation is 'Software Engineer', name starts with 'S', and address contains the word 'Avenue'. Return a dictionary where the keys are the filtered users' names and the values are their occupations.
"""

def filter_users(user_details):
    return dict(sorted(
        {user['name']: user['occupation'] 
         for user in user_details 
         if user['age'] > 25 and 
            user['occupation'] == 'Software Engineer' and 
            user['name'].startswith('S') and 
            'Avenue' in user['address']}.items(), 
        key=lambda x: x[1], reverse=True))