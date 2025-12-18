"""
QUESTION:
Given the mean (μ) and standard deviation (σ) of a normal distribution, and a raw score (X) in that distribution, write a function `calculate_raw_score` that calculates the equivalent raw score in another normal distribution with given mean (μ) and standard deviation (σ) that has the same z-score as the original score. The function should take in the raw score, mean, and standard deviation of the original distribution, and the mean and standard deviation of the new distribution as input.
"""

def calculate_raw_score(midterm_score, midterm_mean, midterm_std_dev, final_mean, final_std_dev):
    z_score = (midterm_score - midterm_mean) / midterm_std_dev
    return z_score * final_std_dev + final_mean