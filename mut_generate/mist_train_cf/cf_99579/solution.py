"""
QUESTION:
Create a function called `create_schedule` that takes a list of tuples, where each tuple contains a speaker's name and their topic of expertise, and returns a list of lists representing the schedule for a three-day conference. The schedule should satisfy the following conditions:
- Each day should have two speeches on different topics.
- No speaker can give two speeches on the same day.
- The speakers should be rotated so that they don't speak in the same order on different days.
"""

def create_schedule(speakers):
    days = []
    topics = ["Technology", "Business", "Social Issues"]
    topic_index = 0
    for i in range(3):
        day = []
        for j in range(2):
            speaker = None
            while speaker is None or speaker in day or (j == 1 and speaker == day[0]):
                speaker = next((s[0] for s in speakers if s[1] == topics[topic_index]), None)
                topic_index = (topic_index + 1) % 3
            day.append(speaker)
        days.append(day)
    return days