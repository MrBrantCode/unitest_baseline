"""
QUESTION:
Write a function called `calculate_annotation_agreement` that calculates the agreement between two raters who annotate emotions in videos. The function should take into account the time aspect of annotations and handle cases where the two raters annotate different numbers of emotions at different times. The function should return a measure of agreement between the two raters. Assume that the input data is a list of tuples, where each tuple contains the time and emotion annotated by each rater.
"""

from collections import defaultdict

def calculate_annotation_agreement(rater1, rater2, window_size):
    """
    Calculate the agreement between two raters who annotate emotions in videos.

    Args:
    rater1 (list of tuples): Time and emotion annotated by rater 1.
    rater2 (list of tuples): Time and emotion annotated by rater 2.
    window_size (float): Size of the time window.

    Returns:
    float: Measure of agreement between the two raters.
    """

    # Create dictionaries to store the emotions annotated by each rater at each time
    rater1_dict = defaultdict(list)
    rater2_dict = defaultdict(list)

    # Populate the dictionaries
    for time, emotion in rater1:
        rater1_dict[time].append(emotion)
    for time, emotion in rater2:
        rater2_dict[time].append(emotion)

    # Initialize variables to store the total number of agreements and disagreements
    agreements = 0
    disagreements = 0

    # Iterate over the times in the first rater's annotations
    for time in rater1_dict:
        # Check if the second rater has an annotation at this time
        if time in rater2_dict:
            # Check if the emotions match
            if rater1_dict[time] == rater2_dict[time]:
                agreements += 1
            else:
                disagreements += 1
        # Check the time window
        for t in range(int(time - window_size), int(time + window_size) + 1):
            # Check if the second rater has an annotation in the time window
            if t in rater2_dict:
                # Check if the emotions match
                if rater1_dict[time] == rater2_dict[t]:
                    agreements += 1
                    break
        else:
            disagreements += 1

    # Calculate the agreement coefficient
    if agreements + disagreements == 0:
        return 0
    else:
        return agreements / (agreements + disagreements)