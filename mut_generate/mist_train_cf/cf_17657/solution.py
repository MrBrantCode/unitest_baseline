"""
QUESTION:
Create a function `process_movie_data` that takes in a pandas DataFrame `dataset` containing movie information with columns 'genre', 'rating', and 'duration'. Calculate and return the following:
- The average rating for each genre of movies.
- The movie with the highest rating in each genre.
- A new dataset including only the movies with a rating above 8 and a duration between 90 and 120 minutes.
- The average duration for movies in each genre, excluding movies with a duration less than 60 minutes.

Assume the input DataFrame is not empty and contains only numeric data in the 'rating' and 'duration' columns, and string data in the 'genre' column.
"""

import pandas as pd

def process_movie_data(dataset: pd.DataFrame) -> tuple:
    """
    Process movie data to calculate various statistics.

    Args:
    dataset (pd.DataFrame): A pandas DataFrame containing movie information.

    Returns:
    tuple: A tuple containing average ratings for each genre, highest rated movies in each genre,
           new dataset with filtered movies, and average duration for each genre.
    """

    # Calculate the average rating for each genre of movies
    average_ratings = dataset.groupby('genre')['rating'].mean()

    # Identify the movie with the highest rating in each genre
    highest_rated_movies = dataset.loc[dataset.groupby('genre')['rating'].idxmax()]

    # Create a new dataset with movies with rating above 8 and duration between 90 and 120 minutes
    new_dataset = dataset.loc[(dataset['rating'] > 8) & (dataset['duration'] >= 90) & (dataset['duration'] <= 120)]

    # Calculate the average duration for movies in each genre, excluding movies with duration less than 60 minutes
    average_durations = dataset.loc[dataset['duration'] >= 60].groupby('genre')['duration'].mean()

    return average_ratings, highest_rated_movies, new_dataset, average_durations