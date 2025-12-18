"""
QUESTION:
Define a function `modify_coda` that takes in two parameters: a list of song lyrics and a new time signature. The function should modify the lyrics by inserting the new time signature at the line immediately after the line that starts with "Coda:". The function should return the modified lyrics.
"""

def modify_coda(lyrics, new_time_signature):
    coda_index = lyrics.index("Coda:")
    lyrics.insert(coda_index + 1, new_time_signature)
    return lyrics