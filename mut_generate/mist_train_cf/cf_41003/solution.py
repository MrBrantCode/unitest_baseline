"""
QUESTION:
Write a function `retrieve_video_url_suffix(metadata, target_duration)` that takes in the following parameters:
- `metadata`: A list of dictionaries, where each dictionary contains the keys 'duration' and 'url_suffix'.
- `target_duration`: An integer representing the target duration for which the URL suffix needs to be retrieved.

The function should return the URL suffix of the video that matches the target duration or the closest duration if an exact match is not found. If multiple videos have durations that are equally close to the target duration, return the URL suffix of the video with the earliest occurrence in the metadata list.
"""

def retrieve_video_url_suffix(metadata, target_duration):
    closest_duration_diff = float('inf')
    closest_url_suffix = None

    for video in metadata:
        duration_diff = abs(video['duration'] - target_duration)
        if duration_diff < closest_duration_diff or (duration_diff == closest_duration_diff and metadata.index(video) < metadata.index(closest_url_suffix) if closest_url_suffix is not None else True):
            closest_duration_diff = duration_diff
            closest_url_suffix = video

    return closest_url_suffix['url_suffix']