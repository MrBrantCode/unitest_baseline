"""
QUESTION:
Implement a Flask API with four endpoints: 

Create a function `get_movies` that responds to `GET /movies`, returning a list of all movies. 

Create a function `add_movie` that responds to `POST /movies`, adding a new movie with the following attributes: title (string), director (string), genre (string), and release_year (integer). The function should return a JSON message indicating that the movie was added successfully.

Create a function `update_movie` that responds to `PUT /movies/<movie_id>`, updating an existing movie by its ID. The function should update the movie's attributes and return a JSON message indicating that the movie was updated successfully. If the movie is not found, it should return a JSON error message with a 404 status code.

Create a function `delete_movie` that responds to `DELETE /movies/<movie_id>`, deleting a movie by its ID. The function should remove the movie from the collection and return a JSON message indicating that the movie was deleted successfully. If the movie is not found, it should return a JSON error message with a 404 status code.

Note that the movie IDs are unique integers assigned to each movie upon creation, and the movie collection is initially empty.
"""

def get_movies(movies):
    """Returns a list of all movies."""
    return movies

def add_movie(movies, new_movie):
    """Adds a new movie with the given attributes to the collection."""
    movies.append(new_movie)
    return {"message": "Movie added successfully"}

def update_movie(movies, movie_id, updates):
    """Updates an existing movie by its ID with the given attributes."""
    for movie in movies:
        if movie.get('id') == movie_id:
            movie.update(updates)
            return {"message": "Movie updated successfully"}
    return {"error": "Movie not found"}

def delete_movie(movies, movie_id):
    """Deletes a movie by its ID from the collection."""
    for movie in movies:
        if movie.get('id') == movie_id:
            movies.remove(movie)
            return {"message": "Movie deleted successfully"}
    return {"error": "Movie not found"}