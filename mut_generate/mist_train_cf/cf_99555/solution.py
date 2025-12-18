"""
QUESTION:
Write a function `get_top_recommendations` that takes a user and two dictionaries as input: `user_interests` and `mutual_friends`. The function should return a list of the top 5 recommended friends for the given user based on their interests and mutual friends. The `user_interests` dictionary maps each user to a list of their interests, and the `mutual_friends` dictionary maps each user to a list of their mutual friends. The function should return the friends with whom the user shares the most interests.
"""

def get_top_recommendations(user, user_interests, mutual_friends):
    user_interests_set = set(user_interests[user])
    recommendations = {}
    for friend in mutual_friends[user]:
        friend_interests_set = set(user_interests[friend])
        common_interests = user_interests_set.intersection(friend_interests_set)
        num_common_interests = len(common_interests)
        if num_common_interests > 0:
            recommendations[friend] = num_common_interests
    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    return [x[0] for x in sorted_recommendations][:5]