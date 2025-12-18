"""
QUESTION:
Write a function `find_top_three_prime_scorers` that takes a list of dictionaries representing users with 'name' and 'score' attributes and returns the names of the top three users with the highest 'score' attribute that is a prime number, sorted in reverse alphabetical order. The function should have a time complexity of O(n sqrt(k) log k) and a space complexity of O(k), where n is the number of users and k is the highest 'score' attribute among the prime number scores.
"""

import math

def find_top_three_prime_scorers(users):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    top_three_users = []
    highest_scores = [float('-inf')] * 3

    for user in users:
        score = user['score']
        if is_prime(score):
            if score > min(highest_scores):
                lowest_index = highest_scores.index(min(highest_scores))
                highest_scores[lowest_index] = score
                top_three_users.append(user['name'])

    top_three_users.sort(reverse=True)
    return top_three_users