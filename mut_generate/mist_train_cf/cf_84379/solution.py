"""
QUESTION:
Implement a function `categorize_blog_posts` that takes a list of dictionaries representing blog posts, each containing 'title', 'comments', and 'source' keys. The function should filter out posts with more than 50 comments and categorize the remaining posts into a dictionary where each key is a source website and the value is a list of posts from that website.
"""

def categorize_blog_posts(stream_of_blog_posts):
    """
    This function filters out posts with more than 50 comments and categorizes the remaining posts into a dictionary 
    where each key is a source website and the value is a list of posts from that website.

    Args:
        stream_of_blog_posts (list): A list of dictionaries representing blog posts.

    Returns:
        dict: A dictionary where each key is a source website and the value is a list of posts from that website.
    """

    # Filter out posts with more than 50 comments
    filtered_posts = [post for post in stream_of_blog_posts if post['comments'] <= 50]

    # Initialize an empty dictionary to store the categorized posts
    categorized_posts = {}

    # Categorize the filtered posts based on their source website
    for post in filtered_posts:
        # If the source website is not in categorized_posts, add it
        if post['source'] not in categorized_posts:
            categorized_posts[post['source']] = []
        categorized_posts[post['source']].append(post)

    return categorized_posts