"""
QUESTION:
Write a function named `filter_blog_posts` that filters a stream of blog posts and returns a list of posts with 50 comments or less and the word "Python" in the title. The input is a list of dictionaries where each dictionary represents a blog post with 'title' and 'comments' keys.
"""

def filter_blog_posts(blog_posts):
    """
    Filters a stream of blog posts and returns a list of posts with 50 comments or less and the word "Python" in the title.

    Args:
        blog_posts (list): A list of dictionaries where each dictionary represents a blog post with 'title' and 'comments' keys.

    Returns:
        list: A list of filtered blog posts.
    """
    return [post for post in blog_posts if post['comments'] <= 50 and 'Python' in post['title']]