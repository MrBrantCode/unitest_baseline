"""
QUESTION:
Write a function called modify_coda that takes a list of song lyrics and a new time signature as input. The function should find the index of the "Coda:" in the lyrics list, and then insert the new time signature at the line immediately after the "Coda:". The function should return the modified lyrics list.
"""

def modify_coda(lyrics, new_time_signature):
    """
    Modifies the coda of a song by adding a new time signature.

    Args:
        lyrics (list): A list of song lyrics.
        new_time_signature (str): The new time signature to add to the coda.

    Returns:
        list: The modified lyrics with the new time signature added to the coda.
    """
    coda_index = lyrics.index("Coda:")
    lyrics.insert(coda_index + 1, new_time_signature)
    return lyrics