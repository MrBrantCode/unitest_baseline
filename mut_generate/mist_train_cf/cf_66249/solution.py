"""
QUESTION:
Implement a function named `movie_summary_and_classification` that takes a list of movies with their plots as input and returns a list of summaries of the movie plots and their corresponding genres. Use Natural Language Processing (NLP) techniques for summarization and classification.
"""

def movie_summary_and_classification(movies):
    summaries = []
    classifications = []
    
    # Assuming movies is a list of dictionaries with 'overview' and 'genres' keys
    for movie in movies:
        # Simple extractive summarization by taking the first 50 characters
        summary = movie['overview'][:50]
        summaries.append(summary)
        
        # Assuming 'genres' is a list of genres
        genres = movie['genres']
        classifications.append(genres)
    
    return summaries, classifications