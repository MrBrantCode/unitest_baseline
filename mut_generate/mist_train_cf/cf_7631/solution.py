"""
QUESTION:
Write a function called `parse_json_data` that takes a JSON string as input, parses the data, and prints the names of all the users and their friends along with their hobbies. The output should be in the format: "User: {username}, Friends: {friend1}, {friend2}, ..., Hobbies: {hobby1}, {hobby2}, ...". Additionally, the function should calculate and print the average age of each user's friends, the number of users and the number of friends each user has, and the most common hobby among all users. The function should handle nested arrays and objects in the JSON data efficiently, minimizing the time and space complexity.
"""

import json
from collections import Counter

def calculate_average_age(friends):
    total_age = sum([friend["age"] for friend in friends])
    return total_age / len(friends)

def parse_json_data(json_data):
    data = json.loads(json_data)
    users = data["users"]

    # Calculate average age, number of friends, and most common hobby for each user
    for user in users:
        friends = user["friends"]
        user["average_age"] = calculate_average_age(friends)
        user["num_friends"] = len(friends)
        user["most_common_hobby"] = Counter(user["hobbies"]).most_common(1)[0][0]

    # Print the required information
    for user in users:
        print("User:", user["name"])
        print("Friends:", ", ".join([friend["name"] for friend in user["friends"]]))
        print("Hobbies:", ", ".join(user["hobbies"]))
        print("Average Age of Friends:", user["average_age"])
        print("Number of Friends:", user["num_friends"])
        print("Most Common Hobby:", user["most_common_hobby"])
        print()