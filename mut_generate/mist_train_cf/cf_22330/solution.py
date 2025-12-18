"""
QUESTION:
Write a function `calculate_popularity_score` that takes in a list of dictionaries where each dictionary represents a movie with keys 'title', 'rating', and 'votes'. The function should filter out movies with less than 500,000 votes or a rating below 8.5, then calculate a popularity score for each remaining movie based on a weighted average of their ratings and number of votes. The weightage for ratings should be 0.7 and the weightage for votes should be 0.3. The function should return a list of dictionaries, each containing the movie's title, rating, number of votes, and popularity score, sorted in descending order of their popularity scores.
"""

def calculate_popularity_score(movies):
    filtered_movies = [
        {
            'title': movie['title'],
            'rating': movie['rating'],
            'votes': movie['votes'],
            'popularity_score': (0.7 * movie['rating']) + (0.3 * (movie['votes'] / 1000000))
        } 
        for movie in movies 
        if movie['votes'] >= 500000 and movie['rating'] >= 8.5
    ]

    filtered_movies.sort(key=lambda x: x['popularity_score'], reverse=True)
    return filtered_movies