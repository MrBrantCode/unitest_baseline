"""
QUESTION:
Write a function named `filter_users` that takes a list of user details as input, where each user is represented as a dictionary with 'Name', 'Age', 'Occupation', and 'Address' keys. The function should filter the users based on the following conditions: age is greater than 21, occupation is not 'Engineer', name starts with 'J', and address contains 'Street'. Then, it should sort the filtered users by their addresses in ascending order. Finally, the function should return a dictionary where the keys are the names of the filtered users and the values are their ages.
"""

def filter_users(user_details):
    filtered_users = {}
    
    for user in user_details:
        name = user['Name']
        age = user['Age']
        occupation = user['Occupation']
        address = user['Address']
        
        if age > 21 and occupation != 'Engineer' and name[0] == 'J' and 'Street' in address:
            filtered_users[name] = age
    
    sorted_users = dict(sorted(filtered_users.items(), key=lambda item: [user['Address'] for user in user_details if user['Name'] == item[0]][0]))
    return sorted_users