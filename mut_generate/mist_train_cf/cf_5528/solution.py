"""
QUESTION:
Create a function called `calculate_weighted_score` that determines the top 5 programming languages currently in use, excluding any languages that were released before 2010. The languages should be ranked based on a weighted score calculated from the following criteria:

- Job listings (weightage: 0.4)
- Popularity on coding forums and communities (weightage: 0.2)
- Number of active open-source projects on GitHub (weightage: 0.3)
- Adoption rate in new startups and tech companies (weightage: 0.5)
- Performance benchmarks and efficiency ratings (weightage: 0.6)

The function should return the top 5 programming languages based on the total weighted score.
"""

def calculate_weighted_score(language, job_listings, popularity_on_forums, open_source_projects, adoption_rate, performance_score):
    """
    Calculate the weighted score for a programming language based on job listings, popularity on forums, 
    open-source projects, adoption rate, and performance score.

    Args:
        language (str): The programming language.
        job_listings (int): The number of job listings for the language.
        popularity_on_forums (int): The popularity score of the language on coding forums.
        open_source_projects (int): The number of open-source projects for the language.
        adoption_rate (float): The adoption rate of the language in new startups and tech companies.
        performance_score (float): The performance score of the language.

    Returns:
        float: The weighted score of the language.
    """

    weighted_score = (job_listings * 0.4) + (popularity_on_forums * 0.2) + (open_source_projects * 0.3) + (adoption_rate * 0.5) + (performance_score * 0.6)
    return weighted_score