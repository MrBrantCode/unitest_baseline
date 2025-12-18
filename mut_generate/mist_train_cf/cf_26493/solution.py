"""
QUESTION:
Generate a function `generate_report(users)` that takes a list of strings representing user information in the format "username: date" (YY/MM/DD) and returns a list of strings. Each string in the output list should represent a user and their date in the specified format, where the usernames are sorted in ascending order and the dates are sorted in descending order. Assume the input list is not empty and all user information is valid and in the correct format.
"""

def generate_report(users):
    user_dict = {}
    for user_info in users:
        username, date = user_info.split(": ")
        user_dict[username] = date

    sorted_users = sorted(user_dict.keys())
    sorted_dates = sorted(user_dict.values(), reverse=True)

    report = [f"{user}: {user_dict[user]}" for user in sorted_users]
    return report