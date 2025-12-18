"""
QUESTION:
Write a function named `find_top_three_prime_score_users` that takes a list of dictionaries representing users with 'name' and 'score' attributes, finds the top three users with the highest prime number scores, and returns their names in a list sorted in reverse alphabetical order. The time complexity of this function should be O(n sqrt(k) log k), where n is the number of users and k is the highest prime number score. The space complexity should be O(k).
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_top_three_prime_score_users(data):
    top_three_users = []
    highest_scores = [float('-inf')] * 3

    for user in data:
        score = user['score']
        if is_prime(score):
            # Check if the current user's score is higher than the lowest score in the top three list
            if score > min(highest_scores):
                # Replace the lowest score in the top three list with the current user's score
                lowest_index = highest_scores.index(min(highest_scores))
                highest_scores[lowest_index] = score
                # Add the current user to the top three list
                if user['name'] not in top_three_users:
                    if len(top_three_users) < 3:
                        top_three_users.append(user['name'])
                    else:
                        top_three_users.pop(top_three_users.index(min(top_three_users)))
                        top_three_users.append(user['name'])

    # Sort the names in reverse alphabetical order
    top_three_users.sort(reverse=True)
    return top_three_users