"""
QUESTION:
Create a function `filter_and_sort_posts` that takes a list of dictionaries representing blog posts, where each dictionary contains a 'title' and a 'comments' key, with the 'title' being a string and the 'comments' being an integer. The function should return a list of titles of posts that have more than 100 comments and the word "Python" in the title, sorted by the number of comments in descending order.
"""

def filter_and_sort_posts(stream_of_blog_posts):
    return sorted([post['title'] for post in stream_of_blog_posts if post['comments'] > 100 and 'Python' in post['title']], key=lambda post: [p['comments'] for p in stream_of_blog_posts if p['title'] == post][0], reverse=True)