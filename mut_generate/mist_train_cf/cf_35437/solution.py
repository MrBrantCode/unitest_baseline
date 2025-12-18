"""
QUESTION:
Implement a function `detect_drowsiness(ear_values)` that takes a list of Eye Aspect Ratio (EAR) values representing consecutive frames and returns `True` if drowsiness is detected and `False` otherwise, using the given constants `EAR_thresh` and `EAR_consec_frames`. The function should analyze the `ear_values` list and determine if the person's eyes have been closed for `EAR_consec_frames` or more consecutive frames, with each frame having an EAR value below `EAR_thresh`.
"""

EAR_thresh = 0.3
EAR_consec_frames = 48

def detect_drowsiness(ear_values):
    counter = 0
    for ear in ear_values:
        if ear < EAR_thresh:
            counter += 1
            if counter >= EAR_consec_frames:
                return True
        else:
            counter = 0
    return False