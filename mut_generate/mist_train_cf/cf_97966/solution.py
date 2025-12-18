"""
QUESTION:
Create a function called `get_user_by_location` that takes in a dictionary `data` and a string `location_name`. The dictionary `data` contains two lists: `users` and `locations`. Each user in `users` has an `id`, `name`, and `email`, and each location in `locations` has an `id` and `name`. Return a list of dictionaries containing user information for the users whose locations match the specified location name. If there is no user with the specified location, return an empty list.
"""

def get_user_by_location(data, location_name):
    users = []
    for user in data['users']:
        for location in data['locations']:
            if user['location_id'] == location['id'] and location['name'] == location_name:
                users.append(user)
    return users