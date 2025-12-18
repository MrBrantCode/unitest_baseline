"""
QUESTION:
Write a function named `find_most_suitable_language` that determines the most suitable programming language for creating a high-performance web application based on a set of criteria. The function should take two parameters: `languages` and `weights`. 

`languages` is a dictionary where the keys are the names of programming languages and the values are dictionaries containing the scores for the following criteria: performance, scalability, security, ease of use, and community support.

`weights` is a dictionary where the keys are the names of the criteria and the values are the corresponding weights, with higher weights indicating higher importance.

The function should rank the programming languages based on these criteria and return the most suitable language. If there is a tie, the function should consider the following additional factors in order of priority: available frameworks and libraries, compatibility with popular web servers, and developer job market demand. 

Note that the additional factors are not provided in the input, so the function should return one of the tied languages.
"""

def find_most_suitable_language(languages, weights):
    def calculate_total_score(language):
        total_score = 0
        for factor, weight in weights.items():
            total_score += language[factor] * weight
        return total_score

    ranked_languages = []
    for language, details in languages.items():
        total_score = calculate_total_score(details)
        ranked_languages.append((language, total_score))
    ranked_languages.sort(key=lambda x: x[1], reverse=True)

    most_suitable_languages = [ranked_languages[0][0]]
    max_score = ranked_languages[0][1]
    for i in range(1, len(ranked_languages)):
        if ranked_languages[i][1] == max_score:
            most_suitable_languages.append(ranked_languages[i][0])
        else:
            break
    if len(most_suitable_languages) == 1:
        return most_suitable_languages[0]
    else:
        for language in most_suitable_languages:
            if language in languages:
                return language
        return most_suitable_languages[0]