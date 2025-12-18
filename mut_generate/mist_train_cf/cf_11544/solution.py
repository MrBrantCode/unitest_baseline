"""
QUESTION:
Write a function `filter_blog_posts` that takes a list of blog posts as input, where each post is a dictionary with 'title' and 'comments' as keys. The function should return a new list containing only the posts with 50 or fewer comments and the word 'Python' in the title.
"""

def filter_blog_posts(stream_of_blog_posts):
    return [post for post in stream_of_blog_posts if post['comments'] <= 50 and 'Python' in post['title']]