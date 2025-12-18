"""
QUESTION:
Create a function called `classify_genre` that takes the audio features of a song as input and classifies the song into one of the four genres: rock, country, hip-hop, or pop. The function should use the following audio features for classification: energy, danceability, and acousticness. The classification criteria are as follows: 
- if energy is greater than 0.8 and danceability is greater than 0.7, the genre is pop
- if energy is greater than 0.6 and acousticness is less than 0.3, the genre is rock
- if energy is less than 0.4 and acousticness is greater than 0.5, the genre is country
- otherwise, the genre is hip-hop.
"""

def classify_genre(audio_features):
    """
    Classify a song into one of the four genres (rock, country, hip-hop, or pop) based on its audio features.

    Args:
        audio_features (dict): A dictionary containing the audio features of the song, including 'energy', 'danceability', and 'acousticness'.

    Returns:
        str: The genre of the song.
    """
    if audio_features['energy'] > 0.8 and audio_features['danceability'] > 0.7:
        return 'pop'
    elif audio_features['energy'] > 0.6 and audio_features['acousticness'] < 0.3:
        return 'rock'
    elif audio_features['energy'] < 0.4 and audio_features['acousticness'] > 0.5:
        return 'country'
    else:
        return 'hip-hop'