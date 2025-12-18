"""
QUESTION:
Create a Python function `album_track_count(tracklist)` that takes a dictionary `tracklist` where each key is an artist and each value is another dictionary with album names as keys and track names as values. The function should return a dictionary where keys are album names and values are the number of tracks in each album.
"""

def album_track_count(tracklist):
    album_count = {}
    for artist, albums in tracklist.items():
        for album, tracks in albums.items():
            if album not in album_count:
                album_count[album] = len(tracks)
            else:
                album_count[album] += len(tracks)
    return album_count