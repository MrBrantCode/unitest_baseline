"""
QUESTION:
Create a function named `filter_users` that takes a list of user details, each represented as a dictionary containing the keys 'name', 'age', 'occupation', and 'address'. The function should filter out users whose age is more than 25, occupation is 'Software Engineer', name starts with 'S', and address contains 'Avenue'. The filtered users should be sorted in descending order by age. The function should return a dictionary where the keys are the names of the filtered users and the values are their occupations.
"""

def filter_users(user_details):
    filtered_users = {}

    for user in user_details:
        name = user['name']
        age = user['age']
        occupation = user['occupation']
        address = user['address']

        if age > 25 and occupation == 'Software Engineer' and name.startswith('S') and 'Avenue' in address:
            filtered_users[name] = occupation

    return dict(sorted(filtered_users.items(), key=lambda x: max(user['age'] for user in user_details if user['name'] == x[0]), reverse=True))