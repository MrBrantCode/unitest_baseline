"""
QUESTION:
Write a function `get_top_recommendations` that takes a user and their interests and mutual friends as input. The function should return the top 5 recommended friends for the given user based on their interests and mutual friends. The input format is: 
- user_interests: a dictionary where the keys are user names and the values are lists of their interests.
- mutual_friends: a dictionary where the keys are user names and the values are lists of their mutual friends.
- The function should only consider users who share at least one interest with the given user.
- The function should return a list of the top 5 recommended friends, ordered by the number of common interests in descending order.
"""

def get_top_recommendations(user, user_interests, mutual_friends):
    """
    Returns the top 5 recommended friends for the given user based on their interests and mutual friends.

    Args:
    user (str): The user for whom to get recommendations.
    user_interests (dict): A dictionary where the keys are user names and the values are lists of their interests.
    mutual_friends (dict): A dictionary where the keys are user names and the values are lists of their mutual friends.

    Returns:
    list: A list of the top 5 recommended friends, ordered by the number of common interests in descending order.
    """
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