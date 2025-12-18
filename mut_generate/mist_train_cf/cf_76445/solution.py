"""
QUESTION:
Write a function `predict_movie_genre` that takes a movie review statement as input and returns the predicted movie genre based on the content of the statement. The function should use supervised classification and the prediction should be made based on the language used to describe the film in the statement.
"""

def predict_movie_genre(statement):
    # Assuming a pre-trained machine learning model is used for prediction
    # This is a simplified example using a dictionary for demonstration purposes
    genre_indicators = {
        "thrilling": "Thriller",
        "romantic": "Romance",
        "action": "Action"
    }
    
    # Split the statement into words
    words = statement.split()
    
    # Initialize the predicted genre
    predicted_genre = None
    
    # Iterate over each word in the statement
    for word in words:
        # Remove punctuation from the word
        word = word.strip('.,!?;:"\'')
        
        # Check if the word is a genre indicator
        if word in genre_indicators:
            # Update the predicted genre
            predicted_genre = genre_indicators[word]
    
    # Return the predicted genre
    return predicted_genre