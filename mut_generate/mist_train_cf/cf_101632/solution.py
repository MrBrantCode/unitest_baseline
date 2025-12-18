"""
QUESTION:
Write a function called modify_coda that takes a list of strings representing the lyrics of a song and a new time signature as input. The function should find the index of the "Coda:" line in the lyrics and insert the new time signature on the line immediately after "Coda:". The function should return the modified lyrics. Assume that "Coda:" is present in the lyrics and that the lyrics are in the format shown in the example.
"""

def modify_coda(lyrics, new_time_signature):
    """
    Modify the coda of a song by adding a new time signature.

    Args:
    lyrics (list): A list of strings representing the lyrics of a song.
    new_time_signature (str): The new time signature for the coda.

    Returns:
    list: The modified lyrics with the new time signature added to the coda.
    """
    coda_index = lyrics.index("Coda:")
    lyrics.insert(coda_index + 1, new_time_signature)
    return lyrics