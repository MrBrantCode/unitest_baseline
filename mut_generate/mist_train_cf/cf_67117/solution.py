"""
QUESTION:
Write a function `evaluate_recommender_system` that takes a list of recommended songs and a list of actual songs played by a user, and returns a measure of the system's performance. The measure of performance should be the mean average precision at k (MAP@k), where k is the number of recommended songs.

The function should calculate the average precision at k for each user and then return the mean of these average precisions across all users. The input lists should be of equal length and should contain song IDs. 

Restrictions: The function should handle cases where the actual songs list is empty or contains songs that are not in the recommended songs list.
"""

def evaluate_recommender_system(recommended_songs, actual_songs):
    """
    Calculate the mean average precision at k (MAP@k) of a recommender system.

    Args:
    recommended_songs (list): A list of lists containing song IDs recommended by the system.
    actual_songs (list): A list of lists containing song IDs actually played by users.

    Returns:
    float: The mean average precision at k.
    """
    
    # Initialize the sum of average precisions
    sum_average_precisions = 0
    
    # Iterate over each user's recommended and actual songs
    for recommended, actual in zip(recommended_songs, actual_songs):
        # Calculate the number of recommended songs (k)
        k = len(recommended)
        
        # Initialize the sum of precisions
        sum_precisions = 0
        
        # Initialize the number of relevant songs found
        num_relevant_found = 0
        
        # Iterate over the recommended songs
        for i, song in enumerate(recommended):
            # Check if the song is in the actual songs
            if song in actual:
                # Increment the number of relevant songs found
                num_relevant_found += 1
                
                # Calculate the precision at this point
                precision = num_relevant_found / (i + 1)
                
                # Add the precision to the sum of precisions
                sum_precisions += precision
        
        # Check if there are any actual songs
        if actual:
            # Calculate the average precision for this user
            average_precision = sum_precisions / min(k, len(actual))
        else:
            # If there are no actual songs, set the average precision to 0
            average_precision = 0
        
        # Add the average precision to the sum of average precisions
        sum_average_precisions += average_precision
    
    # Calculate the mean average precision
    mean_average_precision = sum_average_precisions / len(recommended_songs)
    
    return mean_average_precision