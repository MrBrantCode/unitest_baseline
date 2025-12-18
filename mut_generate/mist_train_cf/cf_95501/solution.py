"""
QUESTION:
Write a function named `filter_users` that takes a list of user details as input. The user details should be a list of dictionaries where each dictionary contains the keys 'Name', 'Age', 'Occupation', and 'Address'. The function should return a dictionary where the keys are the names of the filtered users and the values are their ages. The function should filter out the users whose age is more than 21 and whose occupations are not 'Engineer'. It should also only include users whose names start with the letter 'J' and whose addresses contain the word 'Street'. The filtered users should be sorted by their addresses in ascending order.
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
    
    sorted_users = dict(sorted(filtered_users.items(), key=lambda item: [i for i in user_details if i['Name'] == item[0]][0]['Address']))
    return sorted_users