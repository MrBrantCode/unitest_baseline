"""
QUESTION:
Create a function `filter_blog_posts` that takes a list of blog posts as input, where each post is a dictionary containing a 'title' and a 'comments' key. The function should return a list of post titles that have more than 50 comments and contain the word 'Python' in the title, sorted in descending order by the number of comments.
"""

def filter_blog_posts(stream_of_blog_posts):
    return [post['title'] for post in sorted([post for post in stream_of_blog_posts if post['comments'] > 50 and 'Python' in post['title']], key=lambda x: x['comments'], reverse=True)]