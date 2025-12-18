"""
QUESTION:
Create a function named `filter_profanity` that takes in a list of comments and returns a list of comments with profane language filtered out. The function should consider context and variations of profanity, handle multilingual comments, and minimize false positives and false negatives. The function should have a time complexity of O(nlogn) and be able to handle both online and offline scenarios, ensuring real-time detection and filtering of profanity in comments.
"""

def filter_profanity(comments, profanity_list):
    """
    Filter out comments containing profane language from a list of comments.

    Args:
    comments (list): A list of comments to filter.
    profanity_list (list): A list of profane words.

    Returns:
    list: A list of comments with profane language filtered out.
    """
    
    # Preprocess comments
    processed_comments = []
    for comment in comments:
        # Tokenize the comment into individual words
        words = comment.split()
        
        # Normalize the words to lowercase
        words = [word.lower() for word in words]
        
        # Remove punctuation marks and special characters
        words = [''.join(e for e in word if e.isalnum()) for word in words]
        
        # Check for profanity in the comment
        if not any(word in profanity_list for word in words):
            processed_comments.append(comment)
    
    return processed_comments