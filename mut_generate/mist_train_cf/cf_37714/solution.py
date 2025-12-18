"""
QUESTION:
Create a function `extract_video_info(video_files)` that takes a list of video file names as input where each file name is in the format "video_name_resolution.extension". The function should return a dictionary containing the extracted information, with video names as keys and tuples of resolution and extension as values. The function should handle various video file name formats and correctly extract the video name, resolution, and extension from each file name.
"""

def extract_video_info(video_files):
    video_info = {}
    for file_name in video_files:
        video_name, resolution_ext = file_name.split('_')
        resolution, extension = resolution_ext.split('.')
        video_info[video_name] = (resolution, extension)
    return video_info