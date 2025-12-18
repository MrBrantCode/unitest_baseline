"""
QUESTION:
Create a function `rank_programming_languages` that takes in a list of programming languages and their respective scores for five criteria: job listings, popularity on coding forums, open-source projects on GitHub, adoption rate in new startups, and performance benchmarks. Each criterion has a weightage and is scored on a scale of 1 to 5. The function should calculate the total weighted score for each language and return a list of the top 5 languages, ranked in descending order of their total weighted scores, with a release year of 2010 or later.
"""

def rank_programming_languages(languages):
    """
    This function calculates the total weighted score for each language 
    and returns a list of the top 5 languages, ranked in descending order 
    of their total weighted scores, with a release year of 2010 or later.

    Args:
        languages (list): A list of dictionaries containing information about programming languages.
            Each dictionary should have the keys 'name', 'release_year', 'job_listings', 
            'popularity', 'github_projects', 'adoption_rate', and 'performance_benchmarks'.

    Returns:
        list: A list of the top 5 languages, ranked in descending order of their total weighted scores.
    """

    # Define the weightage of each criterion
    weights = {
        'job_listings': 0.2,
        'popularity': 0.2,
        'github_projects': 0.2,
        'adoption_rate': 0.2,
        'performance_benchmarks': 0.2
    }

    # Filter languages released after 2010
    languages = [language for language in languages if language['release_year'] >= 2010]

    # Calculate the total weighted score for each language
    for language in languages:
        language['total_weighted_score'] = (
            language['job_listings'] * weights['job_listings'] +
            language['popularity'] * weights['popularity'] +
            language['github_projects'] * weights['github_projects'] +
            language['adoption_rate'] * weights['adoption_rate'] +
            language['performance_benchmarks'] * weights['performance_benchmarks']
        )

    # Sort languages by their total weighted scores in descending order
    languages.sort(key=lambda x: x['total_weighted_score'], reverse=True)

    # Return the top 5 languages
    return languages[:5]