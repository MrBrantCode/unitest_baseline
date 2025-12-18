"""
QUESTION:
Write a function `translate_to_ori_images(keypoint_results, records)` that takes a list of detected keypoints and their scores, and a NumPy array representing the original images. The function should translate the detected keypoints to their original positions in the images and return two lists: a list of tuples representing the translated keypoints and a list of confidence scores corresponding to the translated keypoints. The keypoints should be in the same order as the original `keypoint_results`. Each keypoint in `keypoint_results` is a tuple (x, y, score), where x and y are the coordinates of the keypoint and score is its confidence score. The translation should be done by multiplying the x and y coordinates by the width and height of the original image respectively.
"""

import numpy as np

def translate_to_ori_images(keypoint_results, records):
    keypoint_vector = []
    score_vector = []
    for keypoint in keypoint_results:
        x, y, score = keypoint
        translated_x = int(x * records.shape[1])  # Translate x coordinate to original image size
        translated_y = int(y * records.shape[0])  # Translate y coordinate to original image size
        keypoint_vector.append((translated_x, translated_y))
        score_vector.append(score)
    return keypoint_vector, score_vector