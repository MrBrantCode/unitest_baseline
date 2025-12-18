"""
QUESTION:
Create a function called `extract_author_info` that takes a string `info_str` as input and returns a dictionary with keys "author" and "author_email" mapped to their respective values. The input string is in the format `author="<NAME>", author_email="<EMAIL>"`, where the author's name and email do not contain any special characters other than letters, spaces, and periods.
"""

def extract_author_info(info_str):
    author_start = info_str.find('author="') + len('author="')
    author_end = info_str.find('"', author_start)
    author = info_str[author_start:author_end]

    email_start = info_str.find('author_email="') + len('author_email="')
    email_end = info_str.find('"', email_start)
    email = info_str[email_start:email_end]

    return {"author": author, "author_email": email}