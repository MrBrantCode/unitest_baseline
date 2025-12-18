"""
QUESTION:
Create a function `get_users` that takes a list of users and returns a dictionary containing a list of user names and pagination metadata. The function should filter users based on optional query parameters `age` and `address`, and support pagination with `page` and `results_per_page` parameters. The function should handle invalid requests and return a JSON response with an error message. The user list should be in the following format: `[{"name": string, "age": int, "email": string, "address": string}, ...]`. The query parameters should be passed as integers or strings, and the pagination metadata should include the total number of users, current page, and results per page.
"""

def get_users(users, age=None, address=None, page=1, results_per_page=10):
    # Filter users based on age and/or address
    filtered_users = [user['name'] for user in users]
    if age:
        filtered_users = [user['name'] for user in users if user['age'] == int(age)]
    if address:
        filtered_users = [user['name'] for user in users if user['address'] == address]

    # Paginate results
    total_users = len(filtered_users)
    start_index = (page - 1) * results_per_page
    end_index = page * results_per_page
    paginated_users = filtered_users[start_index:end_index]

    # Return response
    response = {
        "users": paginated_users,
        "pagination": {
            "total_users": total_users,
            "page": page,
            "results_per_page": results_per_page
        }
    }
    return response