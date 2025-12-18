"""
QUESTION:
Implement a function `calculate_average_score` that takes a list of `VideoScore` objects as input, where each object contains a `video_id` (integer) and a `score` (float), and returns a dictionary where the keys are the `video_id`s and the values are the average scores for each video.
"""

def calculate_average_score(video_scores):
    video_sum = {}
    video_count = {}
    
    for score in video_scores:
        if score.video_id in video_sum:
            video_sum[score.video_id] += score.score
            video_count[score.video_id] += 1
        else:
            video_sum[score.video_id] = score.score
            video_count[score.video_id] = 1
    
    average_scores = {video_id: video_sum[video_id] / video_count[video_id] for video_id in video_sum}
    return average_scores