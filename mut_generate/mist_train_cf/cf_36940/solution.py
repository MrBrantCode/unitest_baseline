"""
QUESTION:
Write a function `viralAdvertising` that takes an integer `n` as input, representing the number of days the ad has been running, and returns the cumulative number of people who have liked the ad at the end of `n` days. The ad is initially shown to 5 people, and each day, half of the people who saw the ad like it and share it with 3 friends, who see the ad the next day. The input `n` is between 1 and 50 (inclusive).
"""

def viralAdvertising(n: int) -> int:
    shared = 5
    liked = 0
    cumulative_likes = 0
    for _ in range(n):
        liked = shared // 2
        cumulative_likes += liked
        shared = liked * 3
    return cumulative_likes