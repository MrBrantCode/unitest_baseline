"""
QUESTION:
Write a function named `parse_animation_frames` that takes a string of comma-separated values representing different video frames of a stop-motion animation as input. The input string is formatted as "image_name.png,timestamp1,timestamp2,timestamp3,..." separated by pipe "|" for each frame. The function should return a dictionary where the keys are the frame numbers (image name without ".png") and the values are lists of the image name and the corresponding timestamps (in seconds) for each image. The function should handle frames with a variable number of timestamps and return an empty list for frames without timestamps.
"""

def parse_animation_frames(frames_str):
    frames_dict = {}
    frames_list = frames_str.split("|")
    for frame in frames_list:
        frame_values = frame.split(",")
        frame_key = frame_values[0].replace(".png", "")
        frames_dict[frame_key] = []
        for value in frame_values[1:]:
            if value:
                frames_dict[frame_key].append([frame_values[0], int(value)])
    return frames_dict