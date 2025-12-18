"""
QUESTION:
Create a function called `get_most_suitable_language` that determines the most suitable programming language for creating a high-performance web application based on the given criteria.

The function should take two parameters:
- `languages`: A dictionary containing the details of each programming language. The keys of the dictionary are the names of the languages, and the values are dictionaries containing the criteria ratings for each language. The criteria ratings are represented as integers between 1 and 10 (inclusive).
- `weights`: A dictionary containing the weights assigned to each criteria. The keys of the dictionary are the criteria names, and the values are positive integer weights.

The function should consider the following criteria: performance, scalability, security, ease of use, and community support. If there is a tie, the function should consider the following additional factors in order of priority: available frameworks and libraries, compatibility with popular web servers, and developer job market demand.

The function should return a string indicating the most suitable language for creating a high-performance web application.
"""

def calculate_total_score(language, weights):
    total_score = 0
    for criteria, rating in language.items():
        total_score += rating * weights.get(criteria, 0)
    return total_score

def get_most_suitable_language(languages, weights):
    max_score = 0
    most_suitable_language = ""
    for language, ratings in languages.items():
        total_score = calculate_total_score(ratings, weights)
        if total_score > max_score:
            max_score = total_score
            most_suitable_language = language
    return most_suitable_language