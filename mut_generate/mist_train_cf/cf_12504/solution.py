"""
QUESTION:
Create a function `get_users_with_posts` that returns a list of users and their associated posts in JSON format. The function should take no arguments and return a JSON object where each user is represented as an object with a 'user' key containing user data and a 'posts' key containing a list of post data.
"""

def get_users_with_posts(users, posts):
    # Combine user and post data
    user_post_data = []
    for user in users:
        user_posts = [post for post in posts if post['user_id'] == user['id']]
        user_post_data.append({
            'user': user,
            'posts': user_posts
        })

    # Prepare and return the response
    response = {
        'users': user_post_data
    }
    return response