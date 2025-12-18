"""
QUESTION:
Write a function named `modify_coda` that takes in a list of lyrics and two time signatures, and returns the modified list of lyrics with the new time signature added to the coda. The function should find the index of the "Coda:" in the lyrics list and insert the new time signature at the next index. The list of lyrics and time signatures are in the format of strings, with the time signatures in the format of "x/y" where x and y are integers.
"""

def modify_coda(lyrics, time_signature, new_time_signature):
    """
    This function modifies the coda of a song by adding a new time signature.
    
    Args:
    lyrics (list): A list of strings representing the lyrics of the song.
    time_signature (str): The current time signature of the song in the format "x/y".
    new_time_signature (str): The new time signature for the coda in the format "x/y".
    
    Returns:
    list: The modified list of lyrics with the new time signature added to the coda.
    """
    # Find the index of the coda in the lyrics list
    coda_index = lyrics.index("Coda:")
    # Add the new time signature to the coda
    lyrics.insert(coda_index + 1, new_time_signature)
    # Return the modified lyrics
    return lyrics